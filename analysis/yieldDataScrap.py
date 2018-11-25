from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib
import urllib3
import xlsxwriter
from urllib.request import urlopen
import sys

def getIndex(year):
    data = []
    temp = []
    final = []
    count = 0

    if year != 2018:
        string1 = "http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=year(NEW_DATE)%20eq%20"
        string2 = str(year)
        url = string1 + string2
    else:
        url = "http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%2011%20and%20year(NEW_DATE)%20eq%202018"

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    req = urllib.request.urlopen(url)
    bsObj = BeautifulSoup(req, "xml");

    if year <= 2001:
        for item in bsObj.findAll('d:BC_3MONTH'):
            temp.append(item.text)
            count += 1

        data.append(temp[count - 1])
        temp=[]
        count = 0
    else:
        for item in bsObj.findAll('d:BC_1MONTH'):
            temp.append(item.text)
            count += 1

        data.append(temp[count - 1])
        temp=[]
        count = 0

    if year <= 2006 and year >= 2002:
        for item in bsObj.findAll('d:BC_20YEAR'):
            temp.append(item.text)
            count += 1

    else:
        for item in bsObj.findAll('d:BC_30YEAR'):
            temp.append(item.text)
            count += 1

    data.append(temp[count - 1])
    results = list(map(float, data))

    if year <= 2006 and year >= 2002:
        slope = (results[1] - results[0]) / 19

    else:
        slope = (results[1] - results[0]) / 29

    final.append(slope)

    print("the index of yield in %i was: %0.07f" % (year, final[0]))
    if final[0] >= 0.11:
        text_file.write("%i: 4\n" % (year))
    elif final[0] >= 0.09 and final[0] < 0.11:
        text_file.write("%i: 3\n" % (year))
    elif final[0] >= 0.06 and final[0] < 0.09:
        text_file.write("%i: 2\n" % (year))
    elif final[0] >= 0.01 and final[0] < 0.06:
        text_file.write("%i: 1\n" % (year))
    else:
        text_file.write("%i: 0\n" % (year))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        getIndex(year)
    else:
        text_file = open("yield.txt", "w")
        for i in range(1990, 2019, 1):
            getIndex(i)
        text_file.close()
