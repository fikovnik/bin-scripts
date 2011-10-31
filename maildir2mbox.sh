#!/bin/sh

if [ "$#" != "1" ]; then
	echo "Usage: $0 <mbox_file>"
	exit 1
fi

MBOX=$1

for file in new/*; do
       formail -I Status: <"$file" >> $MBOX
done
for file in cur/*; do
       formail -a "Status: RO" <"$file" >> $MBOX
done

