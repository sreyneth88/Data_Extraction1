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
			link=[]
			arr = []
			a=[]
			sumLike = 0
			allpost=browser.find_elements_by_css_selector('div > div._nljxa > div> a')
			for g in allpost:
				getallpost=g.get_attribute("href")
				link.append(getallpost)

			for n in link:
					browser.get(n)
					time.sleep(2)
					try:
						name=browser.find_element_by_css_selector('div > a._4zhc5._ook48').get_attribute('textContent')
					except NoSuchElementException:
						name = ""
					try:
						like_nb=browser.find_element_by_css_selector("section._54eek._56o5u > div").get_attribute("textContent")
						like = like_nb.replace("likes","")
						for m in like:
							if m == "k":
								like=like.replace("k","000")
						like=like.strip()
						print like
						like = float(like)
						arr.append(like)
						

					except NoSuchElementException:
						like_nb = ""
			print arr
			sumLike = sum(arr)
			print sumLike
			avg = sumLike/ len(arr)
			print avg
			a.append(avg)

			obj = {
				"username":name,
				"average":avg
				}
		
			myStr=json.dumps(obj)
			nameFile="avg.json"
			fs = open(nameFile, 'a')
			fs.write(myStr+","+"\n")
		except NoSuchElementException:
			allpost = ""
		
try:
	key=sys.argv[1]
	getUserProfile(key)
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()
	
