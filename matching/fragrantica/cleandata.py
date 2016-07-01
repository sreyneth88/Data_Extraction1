import time
import io
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import selenium
import selenium 
import csv
from selenium.webdriver.support.ui import Select
import urllib
import json
import re

reload(sys)

def cleandata():
	fs = io.open('a.csv', 'a', encoding='utf8')
	with open("AllInvoices.json") as json_file:
		    json_data = json.load(json_file)
		    #print(json_data)
 	for i in json_data:
 		title= i ["title"]
 		#print title
 		cleandata=re.search("(CREAM|Cream|creamy|care|CARE|ZOYA|BODY|body|zoya|Stick|SHAMPOO|Shampoo|shampoo|orly|ORLY|Orly|Body|STICK)", title)
 		# print type(cleandata)
 		if cleandata:
		 	print "have skin|SKIN|EYES|EYE|MAKE|LIP"
		else:
			
			cleannumber=re.sub("[^A-Za-z][\-0-9]+ *(ML)$","",title)
			print cleannumber
			fs.write(cleannumber+"\n")

			

cleandata()