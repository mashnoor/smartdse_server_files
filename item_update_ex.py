#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading, time, urllib, json, httplib, sys, datetime, os, thread
start_time = time.time()
'''
now = datetime.datetime.now()
marketstart = now.replace(hour=10, minute=30, second=0, microsecond=0)
if(marketstart>now):
   # sys.exit()
    pass
'''

my_link_2 = "/var/www/html/dev/smartdsefiles/dse_item_data_ex.py"


def generate_item(item_name, value):
    #f = my_link_2 + " " + item_name + " " +value
    f = "python " + os.path.abspath(my_link_2) + " " + item_name + " " + value
    os.system(f)


my_link = "/var/www/html/dev/smartdsefiles/itemvalues.txt"
my_link_extra = "/var/www/html/dev/smartdsefiles/item_values_extra.txt"

json_data = open(my_link, "r")
json_data_extra = open(my_link_extra, "r")

json_obj = json.load(json_data)
json_obj_extra = json.load(json_data_extra)
json_data.close()
json_data_extra.close()



for i in json_obj:
    generate_item(i["company"], i["value"])
    print i["company"]

for i in json_obj_extra:
    generate_item(i["company"], "n/a")
    print i["company"]
print("--- %s seconds ---" % (time.time() - start_time))
sys.exit()










