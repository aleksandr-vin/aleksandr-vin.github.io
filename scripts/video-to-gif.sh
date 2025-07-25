#!/bin/sh
#
# Credits to http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html

set -e
set -x

VIDEO_FORMAT=mp4

if [[ "$1" != *."${VIDEO_FORMAT}" ]]
then
  echo File type not supported
  exit 11
fi

tmp_file=$(mktemp -t palette)
palette="${tmp_file}.png"

mv "${tmp_file}" "${palette}"

output_dir=.
output_filename="$(basename "${1%%."${VIDEO_FORMAT}"}.gif")"

FFMPEG=/opt/homebrew/bin/ffmpeg

filters="fps=15,scale=-1:-1:flags=lanczos"

"${FFMPEG}" -i "$1" -filter "$filters,palettegen" -y "$palette"
logger -t gif-creator-script "Palette stored in \"$palette\""

FFMPEG -i "$1" -i "$palette" -lavfi "$filters [x]; [x][1:v] paletteuse" -y "$output_dir/$output_filename"
logger -t gif-creator-script "Creating GIF \"$output_filename\" from \"$1\""
