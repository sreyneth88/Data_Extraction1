import json
import pandas

with open("Allproduct.json") as fi:
	safir_name=json.load(fi)
	for key_name in safir_name:
		dic={}
		sub_dictionary=safir_name[key_name]
		for sub_key_name in sub_dictionary:
			if type (sub_dictionary[sub_key_name]) == type(u''):
				string=sub_dictionary[sub_key_name]
				dic[sub_key_name]=string	
			else:	
				dictionary=sub_dictionary[sub_key_name]
				for sub_sub_key_name in dictionary:
					a = sub_key_name +'@'+sub_sub_key_name
					dic[a]=dictionary[sub_sub_key_name]	
		print dic
		print '\n'
		myStr=json.dumps(dic)
		nameFile="a.json"
		fs = open(nameFile, 'a')
		fs.write(myStr+',')

# with open("fproduct.json") as fi :
# 	data=json.load(fi)
# 	data0=data
# 	#print data0

# 	result = {'ratings@'+k:data0[k]  for data0 in [data['24 Platinum ScentStory for women and men']['ratings']] for k in data0}
# 	print result
	
#a = {k:{key if type(safir_name[k][key])==type(u'') else key+'@'+KInD:safir_name[k][key] if type(safir_name[k][key])==type(u'') else safir_name[k][key][KInD] for key in safir_name[k] for KInD in safir_name[k][key]} for k in safir_name }
	#print result