from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib
import urllib3
import xlsxwriter
from urllib.request import urlopen

data = []
temp = []
final = []
count = 0

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
req = urllib.request.urlopen("http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=year(NEW_DATE)%20eq%202009")
bsObj = BeautifulSoup(req, "xml");

for item in bsObj.findAll('d:BC_1MONTH'):
    temp.append(item.text)
    count += 1

data.append(temp[count - 1])
temp=[]
count = 0

for item in bsObj.findAll('d:BC_30YEAR'):
    temp.append(item.text)
    count += 1

data.append(temp[count - 1])
temp=[]
count = 0
results = list(map(float, data))
slope = (results[1] - results[0]) / 29
final.append(slope)
results = []
data = []

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
req = urllib.request.urlopen("http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=year(NEW_DATE)%20eq%202012")
bsObj = BeautifulSoup(req, "xml");

for item in bsObj.findAll('d:BC_1MONTH'):
    temp.append(item.text)
    count += 1

data.append(temp[count - 1])
temp=[]
count = 0

for item in bsObj.findAll('d:BC_30YEAR'):
    temp.append(item.text)
    count += 1

data.append(temp[count - 1])
temp=[]
count = 0
results = list(map(float, data))
slope = (results[1] - results[0]) / 29
final.append(slope)
results = []
data = []

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
req = urllib.request.urlopen("http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=year(NEW_DATE)%20eq%202015")
bsObj = BeautifulSoup(req, "xml");

for item in bsObj.findAll('d:BC_1MONTH'):
    temp.append(item.text)
    count += 1

data.append(temp[count - 1])
temp=[]
count = 0

for item in bsObj.findAll('d:BC_30YEAR'):
    temp.append(item.text)
    count += 1

data.append(temp[count - 1])
temp=[]
count = 0
results = list(map(float, data))
slope = (results[1] - results[0]) / 29
final.append(slope)
results = []
data = []

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
req = urllib.request.urlopen("http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%2011%20and%20year(NEW_DATE)%20eq%202018")
bsObj = BeautifulSoup(req, "xml");

for item in bsObj.findAll('d:BC_1MONTH'):
    temp.append(item.text)
    count += 1

data.append(temp[count - 1])
temp=[]
count = 0

for item in bsObj.findAll('d:BC_30YEAR'):
    temp.append(item.text)
    count += 1

data.append(temp[count - 1])
results = list(map(float, data))
slope = (results[1] - results[0]) / 29
final.append(slope)

print(final)
