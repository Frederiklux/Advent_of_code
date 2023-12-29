#!/bin/bash
value=$(<day6input.txt)

timelimits=($(sed '1q;d' "day6input.txt" | cut -d ':' -f 2 | awk '{$1=$1;print}'))
oldrecords=($(sed '2q;d' "day6input.txt" | cut -d ':' -f 2 | awk '{$1=$1;print}'))

len="${#timelimits[@]}"

for (( i=0; i<$len; i++ )); 
do 
    currentlimit="${timelimits[$i]}"
    currentrecord="${oldrecords[$i]}"
    waystowin=0
    for (( j=0; j<$currentlimit; j++ ));
    do
        buttonhold=$j
        sailtime=$(($currentlimit-$j))
        traveldistance=$(($buttonhold*$sailtime))
        if [[ $traveldistance -ge $currentrecord ]]
        then 
            ((waystowin++))
        fi
    done
    echo "Total ways to win is: " $waystowin
done



#function functionName { echo "hello"; }

#functionName

currentlimit=$(sed '1q;d' "day6input.txt" | sed 's|[^0-9]||g')
currentrecord=$(sed '2q;d' "day6input.txt" | sed 's|[^0-9]||g')

for (( j=0; j<$currentlimit; j++ ));
do
    buttonhold=$j
    sailtime=$(($currentlimit-$j))
    traveldistance=$(($buttonhold*$sailtime))
    if [[ $traveldistance -ge $currentrecord ]]
    then 
        ((waystowin++))
    fi
done
echo "Total ways to win is: " $waystowin