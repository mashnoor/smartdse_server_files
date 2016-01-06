#!/usr/bin/python 
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import urllib2
import time



print "Content-Type: text/plain;charset=utf-8"

response = urllib2.urlopen("http://dsebd.org/index.php")
source = response.read().replace('<font size="+1">', "", 4)
source = source.replace('</font>', "", 4)
# print source

soup = BeautifulSoup(source)
alldivs = soup.find_all('div')
dsex_indexes = []
ds30_indexes = []
totals = []
others = []
for index in range(len(alldivs)):
    try:
        curr_str = str(alldivs[index].string)

        # print(curr_str)

        if curr_str.strip() == "DSEX Index":
            dsex_indexes.append(str(alldivs[index + 1].string).strip())
            dsex_indexes.append(str(alldivs[index + 2].string).strip())
            dsex_indexes.append(str(alldivs[index + 3].string).strip())

        elif curr_str.strip() == "DS30 Index":
            ds30_indexes.append(str(alldivs[index + 1].string).strip())
            ds30_indexes.append(str(alldivs[index + 2].string).strip())
            ds30_indexes.append(str(alldivs[index + 3].string).strip())

        elif curr_str.strip() == "Total Value in Taka (mn)":
            totals.append(str(alldivs[index + 2].string).strip())
            totals.append(str(alldivs[index + 3].string).strip())
            totals.append(str(alldivs[index + 4].string).strip())
        elif curr_str.strip() == "Issues Unchanged":
            others.append(str(alldivs[index + 2].string).strip())
            others.append(str(alldivs[index + 3].string).strip())
            others.append(str(alldivs[index + 4].string).strip())
    except:
        pass
#DSEX Indexes
data1_1 = '{"data1":"' + dsex_indexes[0] + '",'
data2_1 = '"data2":"' + dsex_indexes[1] + '",'
data3_1 = '"data3":"' + dsex_indexes[2] + '"},'


#DS30 Indexes
data1_2 = '{"data1":"' + ds30_indexes[0] + '",'
data2_2 = '"data2":"' + ds30_indexes[1] + '",'
data3_2 = '"data3":"' + ds30_indexes[2] + '"},'


#Trades and Others
ttrade = '{"ttrade":"' + totals[0] + '",'
tvolume = '"tvolume":"' + totals[1] + '",'
tvalue = '"tvalue":"' + totals[2] + '"},'

#Issues
iadvanced = '{"iadvanced":"' + others[0] + '",'
ideclined = '"ideclined":"' + others[1] + '",'
ichanged = '"iunchanged":"' + others[2] + '"},'

#Now find the market status
spans = soup.find_all('span', {'class' : 'green'})
marketstatus = '{"marketstatus":"' + spans[0].string + '"},'

#Server Time
localtime = time.localtime()
timeString = time.strftime("%d %b, %I:%M", localtime)
lastupdate = '{"lastupdate":"' + timeString + '"}'
null_data = '{"data1":"0", "data2":"0", "data3":"0"},'
finalStr =  "[" +  data1_1 + data2_1 + data3_1 + null_data +  data1_2 + data2_2 + data3_2 + ttrade + tvolume + tvalue + iadvanced + ideclined + ichanged + marketstatus + lastupdate + "]"

#Time to write to file!
file = open("/var/www/html/dev/smartdsefiles/homedata.txt", "wb")
print finalStr
file.write(finalStr)
file.close()
