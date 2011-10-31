#!/bin/sh

if [ $# != 2 ]; then
    echo "Usage: $0 <path/to/condor/home> <path/to/condor/config>"
    exit 1
fi

if [ ! -d $1 ]; then
    echo "$1 is not a condor home directory";
    exit 1;
fi

if [ ! -f $2 ]; then
	echo "$2 is not a condor config file";
    exit 1;
fi
export CONDOR_HOME="$1"
export CONDOR_CONFIG=$2
export PATH=$PATH:$CONDOR_HOME/bin:$CONDOR_HOME/sbin

alias cq=condor_q
alias crm=condor_rm
alias cst=condor_status
alias cs=condor_submit 
alias csd=condor_submit_dag

condor_version
