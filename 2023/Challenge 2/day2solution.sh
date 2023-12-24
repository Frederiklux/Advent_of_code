#!/bin/bash
value=$(<day2input.txt)

redlimit=12
greenlimit=13
bluelimit=14

OLDIFS=$IFS
IFS=$'\n'

sum=0

truncate -s 0 games.txt 
for VARIABLE in $value
do
    gamenumber=$(echo $VARIABLE | cut -d ':' -f 1 | tr -d [:alpha:])
    echo "$gamenumber " >> games.txt
done

for VARIABLE in $value 
do
    gamenumber=$(echo $VARIABLE | cut -d ':' -f 1 | tr -d [:alpha:])
    red=$(echo $VARIABLE | cut -d ':' -f 2 | grep -oE '.{,3}red' | tr -d [:alpha:])
    for redballs in $red
    do
        if [ $redballs -le $redlimit ];
        then
            :
        else
            grep -v "$gamenumber " games.txt > temp && mv temp games.txt
            break
        fi;
    done;
    green=$(echo $VARIABLE | cut -d ':' -f 2 | grep -oE '.{,3}green' | tr -d [:alpha:])
    for greenballs in $green
    do
        if [ $greenballs -le $greenlimit ];
        then
            :
        else
            grep -v "$gamenumber " games.txt > temp && mv temp games.txt
            break
        fi;
    done;
    blue=$(echo $VARIABLE | cut -d ':' -f 2 | grep -oE '.{,3}blue' | tr -d [:alpha:])
    for blueballs in $blue
    do
        if [ $blueballs -le $bluelimit ];
        then
            :
        else
            grep -v "$gamenumber " games.txt > temp && mv temp games.txt
            break
        fi;
    done;
done

echo "The answer to day 2 is: $(awk '{s+=$1} END {printf "%.0f\n", s}' games.txt)"