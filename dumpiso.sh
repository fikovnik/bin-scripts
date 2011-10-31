#!/bin/sh

if [ $# != 2 ]; then
	echo "usage: $0 <device> <name.iso>";
	exit 1;
fi

diskutil unmountDisk $1
dd if=$1 of=$2 bs=2048
sleep 3
diskutil mountDisk $1
