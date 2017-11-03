import requests
from bs4 import BeautifulSoup
from NBA_Fanduel_ScrapeHelper import *
import pandas as pd

# Sets up global lists to temporarily store data
dateList = []
GIDList = []
posList = []
nameList = []
starterList = []
FDpointsList = []
FDsalaryList = []
teamList = []
homeAwayList = []
opponentList = []
teamScoreList = []
opponentScoreList = []
minutesList = []
statLineList = []

allLists = [dateList,GIDList,posList,nameList,starterList,FDpointsList,FDsalaryList,teamList,homeAwayList,opponentList,teamScoreList,opponentScoreList,minutesList,statLineList]

url = 'http://rotoguru1.com/cgi-bin/hyday.pl?game=fd&mon=10&day=30&year=2017&scsv=1'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

delimitedData = grabData(soup)

separatedRow = delimitedData.split('\n')[10]

separatedValues = separatedRow.split(';')

numValues = len(separatedValues)

for eachValue in range(0,numValues):
        allLists[eachValue].append(separatedValues[eachValue])

separatedRow2 = delimitedData.split('\n')[11]

separatedValues2 = separatedRow2.split(';')

numValues2 = len(separatedValues2)

for eachValue in range(0,numValues2):
        allLists[eachValue].append(separatedValues2[eachValue])

print allLists

'''

# Iterates through each year of available Fanduel data
for eachYear in range(2011,2018):

    # Grabs the last week so it knows when to stop for current year
    lastWeek = getLastWeek(eachYear)

    # Appends each week of data to global lists
    for eachWeek in range(1,lastWeek+1):
        appendWeek(eachWeek,eachYear,allLists)

Creates CSV for data that has beens scraped

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
df.to_csv("NBA_Optimization/NBA_Fanduel_Historical_Data.csv")

'''