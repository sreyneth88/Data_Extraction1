import json
import csv
import re
import io

txtfile = open('new.txt', 'r')
reader = csv.DictReader( txtfile, "\n")
for all_link in reader:

	cut_link = re.sub(r'(.*)(http.*:\/\/)(\w.*?\.*)(\/)(.*)', r'\3', str(all_link))
	a = unicode(cut_link)
	fs = io.open("new_one.csv", 'a', encoding = 'UTF8')
	fs.write(a + "\n")
    


