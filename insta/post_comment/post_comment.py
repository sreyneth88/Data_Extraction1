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
import re
from selenium.webdriver.support.ui import Select
import urllib
import json
import traceback
from time import gmtime, strftime
import csv
reload(sys)
sys.setdefaultencoding("UTF8")

browser = webdriver.Firefox()

def getUserProfileDetail(url, timestamp):
	browser.get(url)
	gettime=time.strftime("%Y-%m-%d %H:%M:%S")
	url = (browser.current_url)
	try:
		value=[]
		post_comment = browser.find_elements_by_css_selector('div._es1du._rgrbt > ul > li')
		for i in post_comment:
			try:
				username=i.find_element_by_css_selector('a').get_attribute('textContent')
				comment=i.find_element_by_css_selector('span > span').get_attribute('textContent')
				objs={
					"URL":url,
					"Username":username,
					"Comment_text":comment,
					"Datetime":"",
					"timestamp":timestamp
				}
				myStr=json.dumps(objs)
				fs = open("post_comment"+timestamp+".json", 'a')
				fs.write(myStr+","+"\n")

			except NoSuchElementException:
				username = ""
	except NoSuchElementException:
		post_comment = ""
	
try:
	url=sys.argv[1]
	timestamp=sys.argv[2]
	getUserProfileDetail(url, timestamp)
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()
