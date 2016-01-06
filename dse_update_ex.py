#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading, time, urllib, json, datetime, sys, os

now = datetime.datetime.now()

marketstart = now.replace(hour=10, minute=30, second=0, microsecond=0)
if(marketstart>now):
	pass
	#sys.exit()
	


news_link = "/var/www/html/dev/smartdsefiles/generatenews.php"

topitems_link = "/var/www/html/dev/smartdsefiles/topitems.php"
topshares_link = "/var/www/html/dev/smartdsefiles/top20shares.php"
generateitem_link = "/var/www/html/dev/smartdsefiles/generateitemlist.php"
dse30_link = "/var/www/html/dev/smartdsefiles/dse30shares.php"

class dse_up(threading.Thread):

    def __init__ (self, web_link):
        threading.Thread.__init__(self)
        self.web_link = web_link
        

    def run(self):
	
	f =   "php " +  os.path.abspath(self.web_link)
        os.system(f)
        

#thread = dse_up(home_link)
#thread.start()
#time.sleep(1)
#urllib.urlopen(home_link)
thread = dse_up(news_link)
thread.start()
time.sleep(1)
#urllib.urlopen(news_link)
thread = dse_up(topitems_link)
thread.start()
time.sleep(1)
#urllib.urlopen(topitems_link)
thread = dse_up(topshares_link)
thread.start()
time.sleep(1)
#urllib.urlopen(topshares_link)
thread = dse_up(generateitem_link)
thread.start()
#urllib.urlopen(generateitem_link)
thread = dse_up(generateitem_link)
thread.start()
time.sleep(1)
thread = dse_up(dse30_link)
thread.start()
#urllib.urlopen(dse30_link)

'''
import urllib

news_link = "http://localhost/dev/smartdsefiles/generatenews.php"
home_link = "http://localhost/dev/smartdsefiles/substring-home.php"
topitems_link = "http://localhost/dev/smartdsefiles/topitems.php"
topshares_link = "http://localhost/dev/smartdsefiles/top20shares.php"
generateitem_link = "http://localhost/dev/smartdsefiles/generateitemlist.php"
dse30_link = "http://localhost/dev/smartdsefiles/dse30shares.php"



urllib.urlopen(home_link)
urllib.urlopen(news_link)
urllib.urlopen(topitems_link)
urllib.urlopen(topshares_link)
urllib.urlopen(generateitem_link)
urllib.urlopen(dse30_link)
'''
