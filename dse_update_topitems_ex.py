#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, threading, time, urllib, json, datetime, sys

tk = "topitems.php"



class dse_up(threading.Thread):

    def __init__ (self, web_link):
        threading.Thread.__init__(self)
        self.web_link = web_link


    def run(self):
	f = "php /var/www/html/dev/smartdsefiles/topitems.php" #+  os.path.abspath(tk)
	os.system(f)
        #urllib.urlopen(self.web_link).read()


thread = dse_up(tk)
thread.start()
time.sleep(1)

