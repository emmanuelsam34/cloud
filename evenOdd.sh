#!bin/bash

file='numbers.txt'

while read number; do
  remainder=$((number%2))
  if [ $remainder == 0 ]; then
        echo "Number is even"
    else
        echo "Number is odd"
  fi
done < $file
