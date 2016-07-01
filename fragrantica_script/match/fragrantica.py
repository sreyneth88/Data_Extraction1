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
import traceback
from selenium.webdriver.support.ui import Select
import urllib
import json
import unicodedata

PYTHONIOENCODING='utf-8'

reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()

def searching(title):
	browser.get("https://www.google.com/")
	browser.wait = WebDriverWait(browser, 40)
	try:
		search=browser.find_element_by_css_selector("div#gs_lc0 input#lst-ib")
		mydata=title.replace("_"," ")
		re = mydata + " fragrantica"
		search.send_keys(re)
		time.sleep(2)
		try:
			clicksearch = browser.find_element_by_css_selector("div.jsb center input:nth-child(1)")
			clicksearch.click()
			time.sleep(4)
		except NoSuchElementException:
			print "dosen't click search!"
		getpro =""
		mystring = ""
		try:
			
			product=[]
			url=browser.find_element_by_css_selector("div > div > h3 > a").get_attribute('href')
			#print url
			myurl=url.find("http://www.fragrantica.com/perfume/")
			# print type(myurl)
			# fs = io.open('link.csv', 'a', encoding='utf8')
			# fs.write(myurl+"\n")
			
			
			if myurl != -1:
				# browser.get(url)
				# try:
				# 	getpro=browser.find_element_by_css_selector("#col1 > div > div > h1 > span").get_attribute("textContent")
				# 	print getpro
				# 	product.append(getpro)
				# except NoSuchElementException:
				# 	getpro=""
				obj={
					"Product_name":title,
					"Link": url
					#"Fragrantica_product":getpro
				}		
				
				myStr=json.dumps(obj)
				fs = open("fragrantica_product.json", 'a')
				fs.write(myStr+', \n')
			else:
		 			print "No product detail"
			
			
		
		except NoSuchElementException:
			url =""
		
		
	except NoSuchElementException:
		print "cannot search"
		return -1
		time.sleep(2)
	

try:
	title=sys.argv[1]
	searching(title)
	browser.close()
except:
	print "Error"
	traceback.print_exc()
	browser.close()
	