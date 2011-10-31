#!/bin/sh

if [ "$#" != "1" ]; then
	echo "Usage: $0 <user@host>"
	exit 1
fi

UH=$1

ssh $UH "if [ ! -d .ssh ]; then mkdir .ssh; chmod 700 .ssh; fi"
scp ~/.ssh/id_rsa.pub $UH:.ssh
ssh $UH "cat .ssh/id_rsa.pub >> .ssh/authorized_keys; chmod 400 .ssh/authorized_keys"
