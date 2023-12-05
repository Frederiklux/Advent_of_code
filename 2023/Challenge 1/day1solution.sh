#!/bin/bash
value=$(<day1input.txt)
sum=0

for VARIABLE in $value
do
    first=$(echo $VARIABLE | tr -d [:alpha:] | cut -c 1)
    last_numbers=$(echo $VARIABLE | tr -d [:alpha:])
    last=$(echo "${last_numbers: -1}")
    both="$first""$last"
    sum=$(echo $((sum + both)))
    echo $sum
#	eval "first_character$c= $VARIABLE | tr -d [:alpha:] | cut -c1"
done