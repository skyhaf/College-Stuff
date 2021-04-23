#!/bin/bash
filename='input.txt'

while read line; do
# reading each line

# # for i in $line
# # do
# # echo -n "${i[1]} "
# # done

if [[ $line =~ "nasi" ]] || [[ $line =~ "Nasi" ]]
then
    stringarray=($line)
    echo "${stringarray[1]} ${stringarray[3]} ${stringarray[4]}"
else
    continue
fi



done < $filename

# while read line;
# do
#     echo $line
# done < input.txt

# for word in $(sed 4d8d input.txt); do echo $word; done
