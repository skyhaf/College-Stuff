#!/bin/bash
filename='input.txt'

while read line; do

if [[ $line =~ "nasi" ]] || [[ $line =~ "Nasi" ]]
then
    stringarray=($line)
    echo "${stringarray[1]} ${stringarray[3]} ${stringarray[4]}"
else
    continue
fi

done < $filename

