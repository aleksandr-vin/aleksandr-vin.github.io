#!/usr/bin/env bash
#
# Get specific certificate from the server
#

set -e

# Ensure SERVER_HOST is set
: "${SERVER_HOST:?Need to set SERVER_HOST}"

# Subject to match (case-insensitive substring match)
: "${CERT_SUBJECT:?Need to set CERT_SUBJECT to filter by subject}"

# Default port to 443 if not set
SERVER_PORT="${SERVER_PORT:-443}"

cert_dir=$(mktemp -d "${TMPDIR:-/tmp}/XXXXXX")

cleanup() {
    rm -rf -- "${cert_dir}"
}

tmp_file="${cert_dir}/chain.pem"

openssl s_client -showcerts -connect "${SERVER_HOST}:${SERVER_PORT}" < /dev/null \
    | awk '/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/' > "${tmp_file}"

echo >&2 "Saved cert chain to ${tmp_file}"

# Count how many certificates are in the file
cert_count=$(grep -c "BEGIN CERTIFICATE" "${tmp_file}")

# Split manually using awk
awk_script='
  /-----BEGIN CERTIFICATE-----/ {cert++}
  {print > (out_prefix cert ".pem")}
'

out_prefix="${cert_dir}/"

awk -v out_prefix="${out_prefix}" "${awk_script}" "${tmp_file}"

echo >&2 "Extracted ${cert_count} certificates:"
ls -1 "${out_prefix}"*.pem >&2


echo >&2 "Searching for certificate with subject containing: ${CERT_SUBJECT}"

for cert_file in "${out_prefix}"*.pem; do
    subject=$(openssl x509 -in "$cert_file" -noout -subject)
    echo >&2 "${subject}"
    if echo "$subject" | grep -qi "${CERT_SUBJECT}"; then
        echo >&2 "Match found in: $cert_file"
        cat "$cert_file"
        break
    fi
done

cleanup
