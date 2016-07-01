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
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
profile_url=' '

browser = webdriver.Firefox()
def getUserProfile(key):
		url="https://www.instagram.com/"+key
		browser.get(url)
		browser.wait = WebDriverWait(browser, 30)
		try:
			getpost=browser.find_elements_by_css_selector(" div > div._nljxa > div> a")
			print len(getpost)
			for i in getpost:
				getlink=i.get_attribute("href")
				print getlink
				link = io.open('link_userprofile.csv', 'a', encoding='utf8')
				link.write(getlink+"\n")
		except NoSuchElementException:
			getpost = ""

key=sys.argv[1]
getUserProfile(key)
browser.quit()
	
