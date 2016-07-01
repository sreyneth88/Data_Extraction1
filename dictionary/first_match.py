import pandas
import csv
import json
import re
import dict


with open('product.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        searchs = row[2]
        #print searchs
        with open('Allproduct.json') as json_data:
			all_data=json.load(json_data)
			#print all_data
			data=all_data['product_name']
			print data
			l=0

			for i in all_data:

				data=all_data[l]['product_name']
				l = l +1
				myresult=re.search(searchs,data)

				if myresult:

					print "additem"

				else:
					print "Not matched"
		


		
# fragrantica=pandas.read_csv('fragranticaproduct.csv')
# print fragrantica
# print fragrantica[[2]]

# with open('fragranticaproduct.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         search = row[2]
#         print search
    # for i in search:
    # 	print i