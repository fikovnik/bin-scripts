#!/bin/sh

signal="-TERM"

case "$#" in
  1) signal="-TERM"
    name="$1"
    ;;
  2) signal=$1
    name="$2"
    ;;
  *) echo "Usage: $0 [-signal] <process_name_substr>"
    exit 1
    ;;
esac


for pid in `ps ax -o pid= -o comm= | grep -i $name | awk '{print $1}'`; do
  kill $signal $pid
done
