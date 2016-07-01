#!/bin/sh
cat allfollower.csv | while read line
do
    nodejs getProfile.js $line
    wait
done






#run every 2 days
#!/bin/sh
# while [ true ]
# cat allfollower.csv | while read line
# do
#     nodejs getProfile.js $line
#     wait
# done
# sleep 172800   #sleep for 2 days
