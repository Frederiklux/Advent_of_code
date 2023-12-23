#!/bin/bash
value=$(<day2input.txt)

redlimit=12
greenlimit=13
bluelimit=14

OLDIFS=$IFS
IFS=$'\n'

sum=0

for VARIABLE in $value 
do
    gamenumber=$(echo $VARIABLE | cut -d ':' -f 1 | tr -d [:alpha:])
    echo $gamenumber
    red=$(echo $VARIABLE | cut -d ':' -f 2 | grep -oE '.{,3}red' | tr -d [:alpha:])
    for redballs in $red
    do
        if [ $redballs -le $redlimit ];
        then
            echo "Alt er fint";
        else
            echo "Alt er skidt";
        fi;
    done;
    echo $red
done

#record game number DONE
#separate hands in games
#identify correct number with colours
#check identified number with limit
#add game number to sum in case above check succeeds