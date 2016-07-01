#!/bin/bash
echo "Start get link"
cat AllInvoices.csv | while read line
do 
         python fragrantica.py  ${line// /_}
 wait
done
echo "Finished get link"