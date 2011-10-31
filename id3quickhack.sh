#!/bin/sh
#
# id3hack - add track names and numbers to id3 tags
#
if [ "$1" ]
then
  for file
  do
    if [ -e "$file" ]
    then
      id3tool \
        --set-title="$(echo "$file" | sed 's/...\(.*\)\.mp3/\1/')" \
        --set-track="$(echo "$file" | sed 's/\(..\).*/\1/')" \
        "$file"
    else
      echo >&2 "No such file: "$1""
      exit 1
    fi
  done
else
  echo >&2 "Usage: "$(basename "$0")" INPUTFILE [...]"
  exit 1
fi
