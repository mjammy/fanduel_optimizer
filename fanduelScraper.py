import requests
from bs4 import BeautifulSoup
from scrapeHelper import *
import pandas as pd
import numpy as np

weekList = []
yearList = []
GIDList = []
nameList = []
posList = []
teamList = []
homeAwayList = []
opponentList = []
pointsList = []
salaryList = []
allLists = [weekList,yearList,GIDList,nameList,posList,teamList,homeAwayList,opponentList,pointsList,salaryList]

'''
urlTemp = 'http://http://rotoguru1.com/cgi-bin/fyday.pl?week='

firstYear= getFirstYear()
lastYear = getLastYear()

for eachYear in range(firstYear,lastYear+1):

    firstWeek = getFirstWeek()
    lastWeek = getLastWeek(eachYear)

    for eachWeek in range(firstWeek,lastWeek+1):

        url = 'http://http://rotoguru1.com/cgi-bin/fyday.pl?week=' + str(eachWeek) + '&year=' + str(eachYear) + '&game=fd&scsv=1'
        print url

'''

url = 'http://rotoguru1.com/cgi-bin/fyday.pl?week=7&year=2017&game=fd&scsv=1'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Grab Data
delimitedData = grabData(soup)

# Turn it into list of rows
appendData(delimitedData,allLists)

print allLists
    



