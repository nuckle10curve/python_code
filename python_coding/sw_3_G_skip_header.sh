#!/bin/bash

i=0
NAMES="$(< in_3_B.csv)" #names from names.txt file
for NAME in $NAMES; 
do
    if [ $i != 0 ]; then
     echo $NAME >>output/rpt_3_G.txt
     echo "writing"
    fi
   (( i=i+1 ))
done 