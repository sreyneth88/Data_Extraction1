#!/bin/bash
echo "Start extract link menu"
cat name.csv | while read line
do
        python getblog.py ${line// /_}

        #echo $line
        #echo ${line// /_}
 wait
done
echo "successful extract linkproduct"
