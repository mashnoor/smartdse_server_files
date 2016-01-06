
import json
from requests_futures.sessions import FuturesSession

# max workers set to 10, default is 2
session = FuturesSession(max_workers=10)

f = open("/var/www/html/dev/smartdsefiles/allitems.txt", "r")

items = json.load(f)
f.close()

def get_url(item_name):
    base_url = "http://www.dsebd.org/displayCompany.php?name="
    return  base_url + item_name

all_links = []
all_items = []
for item in items:
    all_links.append(get_url(item["company"]))
    all_items.append(item["company"])

all_sessions = []


#make sessions
for link in all_links:
    curr_session = session.get(link)
    all_sessions.append(curr_session)


#get the responses
i = 0
for msession in all_sessions:
    response = msession.result()
    f = open("/var/www/html/dev/smartdsefiles/Sources/" + all_items[i] + ".txt", "w+")
    f.write(response.text)
    f.close()
    i+=1
    print (response.status_code)

