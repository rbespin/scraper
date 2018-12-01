#!/bin/bash
NOCHANGE="Failure: No Change"
CHANGE="Success: Change"
RESULT=$(diff recentrun.txt archive.txt)
if [ $? -eq 0 ] 
then
   echo $NOCHANGE
else
    echo $CHANGE
	cat recentrun.txt
fi

