import json
import csv
import pandas


with open("newProducts.json") as json_data:
	f = json.load(json_data)
	l = []
	for i in f:
		print i['_id']


# l={}
# for i in d:
# if i['category']=='DYq5Z8GmZZ6wyMmWj':
# l[i['_id']]=i['title']
# print l
# l.values()
# len(l)
# for key in l:
# if l[key] in df['ItemName']:
# print l[key]
# all_product_collected={'id':list(l.keys()),'ItemName':list(l.values)}
# list(l.keys()),
# list(l.values)
# all_product_collected={'id':list(l.keys()),'ItemName':list(l.values())}
# df2=pandas.Dataframe(all_product_collected)
# df2=pandas.DataFrame(all_product_collected)
# df2.to_csv('safir_product_collected.csv')
# df2.to_csv('safir_product_collected.csv',encode='utf-8')
# df2['ItemName'].drop_duplicates()
# df2['ItemName']
# len(df2['ItemName'])
# len(df2['ItemName'].drop_duplicates())
# len(df2['_id'].drop_duplicates())