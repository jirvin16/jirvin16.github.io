#!/bin/sh
 
jekyll serve

# I don't think this is necessary
# rm -rf public_html/

# Upload to server
# scp -r _site/* public_html/

echo "cat git_password to get pw for git push"
