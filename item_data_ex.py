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

my_link_2 = "dse_item_data_ex.py"


def generate_item(item_name, value):
    f = "python " + os.path.abspath(my_link_2) + " " + item_name + " " + value
    os.system(f)


my_link = "itemvalues.txt"
my_link_extra = "item_values_extra.txt"

json_data = open(my_link, "r")
json_data_extra = open(my_link_extra, "r")

json_obj = json.load(json_data)
json_obj_extra = json.load(json_data_extra)
json_data.close()
json_data_extra.close()
k = 0

for i in json_obj:
    thread.start_new_thread(generate_item, (i["company"], i["value"]))
    k+=1
    print i['company']
    if (k==3):
        time.sleep(2)
        k=0



for i in json_obj_extra:

        try:
            thread.start_new_thread(generate_item, (i["company"], "n/a"))

        except:
           print i["company"] + " Has error!@"

        k+=1

        if (k==3):
            time.sleep(2)
            k=0
        print i["company"]



print("--- %s seconds ---" % (time.time() - start_time))
sys.exit()


print("--- %s seconds ---" % (time.time() - start_time))









