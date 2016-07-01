#!/bin/bash
echo "Start read folder"
cat sephora.csv | while read line
do
        python readfolder.py ${line// /_}

 wait
done
echo "successful extract read folder"
