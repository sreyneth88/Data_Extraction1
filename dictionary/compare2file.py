import json
import pandas
import unicodedata

PYTHONIOENCODING='utf-8'

with open('allProductClean.json') as json_data:
	all_data=json.load(json_data)
	l = 0
	for i in all_data:
		#
		f=all_data[l]['product_name']
		#print f
		l = l + 1

d={ f['product_name']:f for f in all_data }
#print d

fragrantica=pandas.read_csv('fragranticaproduct.csv',header=None)
#print fragrantica[2][0]
fragrantica[2][8]
	
L=len(fragrantica[2])
for l in range(L):
	product_name_tmp=fragrantica[2][l]
#	print product_name_tmp
	if product_name_tmp in d.keys():
		dictionarytmp=d[product_name_tmp]
		print dictionarytmp
		dictionarytmp['safir_name']=fragrantica[0][l]
		print dictionarytmp
		dictionarytmp['category']="Perfume"
		print dictionarytmp
		d[product_name_tmp]=dictionarytmp
		print d

myStr=json.dumps(d)
nameFile="Allproduct.json"
fs = open(nameFile, 'a')
fs.write(myStr)


# dict_list = [{"Al Hajjar Al Aswad Abdul Samad Al Qurashi for men":{"pyramid": "test"}}]
# dictionary = {}
# for i, d in d enumerate(dict_list):
#     dictionary[i] = d
#     print dictionary


# fragrantica
# { f['product_name']: for f in fragrantica }

# d=[]
# for f in all_data:
# 	d[f['product_name']]=f