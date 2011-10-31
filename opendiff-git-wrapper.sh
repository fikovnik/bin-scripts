#!/bin/sh
echo "$2" > /tmp/a
/usr/bin/opendiff "$2" "$5" -merge "$1"

