#!/bin/sh

rm -rf public_html/

# Upload to server
scp -r _site/* public_html/

