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

urlTemp = 'http://rotoguru1.com/cgi-bin/fyday.pl?week='

firstYear= getFirstYear()
lastYear = getLastYear()

for eachYear in range(firstYear,lastYear+1):

    firstWeek = getFirstWeek()
    lastWeek = getLastWeek(eachYear)

    for eachWeek in range(firstWeek,lastWeek+1):

        url = urlTemp + str(eachWeek) + '&year=' + str(eachYear) + '&game=fd&scsv=1'
        print url

        # Get all inner HTML using requests/BeautifulSoup
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Grab Data
        delimitedData = grabData(soup)

        # Append all data into a set of lists
        appendData(delimitedData,allLists)

        print("Appended: Year - " + str(eachYear) + ", Week - " + str(eachWeek))

''' Creates CSV for data that has beens scraped '''

# Turns our lists into a dict
d = {   "Year" : yearList,
        "Week" : weekList,
        "Position" : posList,
        "Player" : nameList,
        "Team" : teamList,
        "H/A" : homeAwayList,
        "Opponent" : opponentList,
        "Points" : pointsList, 
        "Fanduel Salary" : salaryList }

# Makes dataframe consisting of the columns in dict
df = pd.DataFrame(d)

# Converts the dataframe to a csv
df.to_csv("allHistoricalFanduelData.csv")


