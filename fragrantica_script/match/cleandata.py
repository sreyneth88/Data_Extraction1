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
	fs = io.open('data.csv', 'a', encoding='utf8')
	with open("testa.json") as json_file:
		    json_data = json.load(json_file)
		    #print(json_data)
 	for i in json_data:
 		itemname= i ["itemname"]
 		#print title
 		cleandata=re.search("(nail|Nail|NAIL|skin|SKIN|EYES|EYE|MAKE|LIP|FOAM|SKINTONE|LIPSTICK|PENCIL|MASCARA|LOTION|POWDER|LAQUE|HAIR|BLUSH|GLOSS|VERNIS|BRUSH|TEINT|NAIL|NOUBA|EYESHADOW|LINER|POLISH|PHYTOMER|LIP|LIPSTICK|BODY|CREAM|Cream|creamy|care|CARE|ZOYA|BODY|body|zoya|Stick|SHAMPOO|Shampoo|shampoo|orly|ORLY|Orly|Body|STICK|Lipstick|lipstick)", itemname)
 		# print type(cleandata)
 		if cleandata:
		 	print "have skin|SKIN|EYES|EYE|MAKE|LIP"
		else:
			
			cleannumber=re.sub("[^A-Za-z][\-0-9]+ *(ML)$","",itemname)
			#print cleannumber
			fs.write(cleannumber+"\n")

			

cleandata()