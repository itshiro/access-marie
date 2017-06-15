# -*- coding: utf-8 -*- 
##
## BeautifulSoup使ってXpath使う破片
##
import urllib3
import lxml.html
import json
import datetime
import time


## SUBARU
urls = {
	'Marie'	    :'http://marie-cf.itshiro.club'
}


xpaths = {
	'current':"//div[1]/span[@class='stock_price']",
	'target':"//div[@class='cell md_target_box_price']",
	'logial/estimated':"//span[@class='fsl fwb']"
}

http = urllib3.PoolManager()

for i in range(1000):
	for name in urls:
#	print company
		url = urls[name]
		response = http.request('GET',url)
		html = response.data
		print html
		time.sleep(3)
