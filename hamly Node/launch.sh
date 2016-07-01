#!/bin/bash
echo "Start get link"
cat allfollower.csv | while read line
do 
         nodejs getFollower.js $line
 wait
done
echo "Finished get link"
