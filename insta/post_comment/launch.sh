#!/bin/bash

while true; 
echo "Start user_profile Top post" 

        python user_post.py $1

echo "Finished user profile"

do 
timestamp=$(date +%s) 
echo $timestamp

	echo "Start user_profile_detail after with top post"

	cat link_userprofile.csv | while read line
	do
			
	        python post_comment.py $line  $timestamp
	 wait
	done
	echo "successful user_profile_detail" 
done

