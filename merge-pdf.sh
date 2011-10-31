#!/bin/bash

output=$1
shift 1

"/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py" -o $output $@
