#!/usr/bin/env bash
#
# Stripping metadata and resizing to 1024x1024 max sizes
#

set -x
set -e

for i in img/*.HEIC
do
  magick $i -resize 1024x1024\> -strip ${i%%.HEIC}.JPG
  ls -l $i ${i%%.HEIC}.JPG
done
