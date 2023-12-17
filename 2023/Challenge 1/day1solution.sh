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
#	eval "first_character$c= $VARIABLE | tr -d [:alpha:] | cut -c1"
done

echo "The first answer is:" $sum


cp day1input.txt day1input2.txt

# replace text with digits
sed -i -e 's/one/one1one/g' day1input2.txt
sed -i -e 's/two/two2two/g' day1input2.txt
sed -i -e 's/three/three3three/g' day1input2.txt
sed -i -e 's/four/four4four/g' day1input2.txt
sed -i -e 's/five/five5five/g' day1input2.txt
sed -i -e 's/six/six6six/g' day1input2.txt
sed -i -e 's/seven/seven7seven/g' day1input2.txt
sed -i -e 's/eight/eight8eigth/g' day1input2.txt
sed -i -e 's/nine/nine9nine/g' day1input2.txt
sed -i -e 's/ten/ten10ten/g' day1input2.txt

value2=$(<day1input2.txt)
sum=0

for VARIABLE in $value2
do
    first=$(echo $VARIABLE | tr -d [:alpha:] | cut -c 1)
    last_numbers=$(echo $VARIABLE | tr -d [:alpha:])
    last=$(echo "${last_numbers: -1}")
    both="$first""$last"
    sum=$(echo $((sum + both)))
#	eval "first_character$c= $VARIABLE | tr -d [:alpha:] | cut -c1"
done

echo "The second answer is:" $sum