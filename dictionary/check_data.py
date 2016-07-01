import json
import pandas
import csv

keyname=[]
with open('MainProduct.json') as json_data:
	alldata = json.load(json_data)
	for key_name in alldata:
		dictionary = alldata[key_name]

		for sub_key_name in dictionary:
			keyname.append(sub_key_name)
			value = dictionary[sub_key_name]
			

#print type(keyname)
new_dictionary={}
for newkey in keyname:
	new_dictionary[newkey]=[]

for safir_name in alldata:
	currentdict=alldata[safir_name]

	for attribute in new_dictionary:
		
		data_check = attribute in currentdict

		if data_check== False:

			new_dictionary[attribute].append(0) 
		else:
			new_dictionary[attribute].append(currentdict[attribute])
		

		#print new_dictionary,'\n'

	#print 'NEW ITERATION\n'
	print new_dictionary
	myStr=json.dumps(new_dictionary)
	nameFile="Dictionary_data.json"
	fs = open(nameFile, 'a')
	fs.write(myStr)			
	
#print new_dictionary


# new_dictionary={}
# # print type({})
# # print new_dictionary
# new_dictionary["key_name"]=[]
# # print type([])
# # print new_dictionary
# #myString="Mandarin"
# new_dictionary["key_name"]=[keyname]
# #keyname.append(myString)
# #print new_dictionary
# new_dictionary['key_name'].append(new_dictionary)
# print new_dictionary

