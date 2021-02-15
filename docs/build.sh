#!/bin/bash

# This script does an incremental build to account for the fact that we cannot
# do one bundle exec jekyll build as it runs out of memory. Intstead, we copy
# files from the _staging folder and move them into _packages and then do
# an incremental build.

# First remove any files > 1MB, we can't include that much code (should only
# be one file with a bunch of javascript and maps

find _staging/ -type f -size +1M -delete

for char in "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"; do
    echo "Processing $char"
    mv _staging/$char*.md _packages/
    if [ "$?" == 0 ]; then
        bundle exec jekyll build --incremental --profile
    fi
done

# Move the rest of files (if and odd names)
mv _staging/*.md _packages/
if [ "$?" == 0 ]; then
    bundle exec jekyll build --incremental --profile
fi
