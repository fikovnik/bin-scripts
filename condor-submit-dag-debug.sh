#!/bin/sh

if [ $# != 1 ]; then
	echo "Usage: $0 <dag>"
	exit 1
fi

DAG="$1"
SUBMIT="$DAG.condor.sub"

if [ -f $SUBMIT ]; then
	rm $SUBMIT;
fi

condor_submit_dag -no_submit $DAG > /dev/null

ENVIRONMENT=`awk -F" " '/environment/ { gsub(/^[ ]*"|"[ ]*$/,"",$3); print $3; }' $SUBMIT`
ENVIRONMENT=`echo "$ENVIRONMENT" | awk -F";" '{ for (i=1;i<=NF;i++) { print $i; } }'`
EXECUTABLE=`awk -F= '/executable/ { gsub(/^[ ]*"|"[ ]*$/,"",$2); print $2; }' $SUBMIT`
ARGUMENTS=`awk -F= '/arguments/ { gsub(/^[ ]*"|"[ ]*$/,"",$2); gsub(/\\$/,"\\\\$",$2); print $2; }' $SUBMIT`
    
CMD="$ENVIRONMENT $EXECUTABLE $ARGUMENTS -WaitForDebug"
echo $CMD
eval $CMD
