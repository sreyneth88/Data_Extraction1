import csv
import re
import io
import json

fs= io.open('farsi.csv', 'w', encoding='utf8')
fs2= io.open('charactor.csv', 'w', encoding='utf8')


with open('all_product_to_collect.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        byrow=(row['Barcode'],row['ItemName'])
        getrow=row['Barcode']+" "+row['ItemName']
        getrow=re.sub(r'\s+','',getrow)
        # print getrow
        data=re.search("[^0-9a-zA-Z\&\-\|\-\+\-\'\-\#\-\-\-\.\-\^\-\*\-\_\-\()\-\/\-\%\-\`]",getrow)

        if data:

            f1=row['Barcode']+", "+row['ItemName']
            fs.write(f1.decode("utf-8")+"\n")
            
        else:
            f2=row['Barcode']+","+row['ItemName']
            fs2.write(f2.decode("utf-8")+"\n")