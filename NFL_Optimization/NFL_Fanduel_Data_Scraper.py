import requests
from bs4 import BeautifulSoup
from NFL_Fanduel_ScrapeHelper import *
import pandas as pd

# Sets up global lists to temporarily store data
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

# Iterates through each year of available Fanduel data
for eachYear in range(2011,2018):

    # Grabs the last week so it knows when to stop for current year
    lastWeek = getLastWeek(eachYear)

    # Appends each week of data to global lists
    for eachWeek in range(1,lastWeek+1):
        appendWeek(eachWeek,eachYear,allLists)

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
df.to_csv("NFL_Optimization/NFL_Fanduel_Historical_Data.csv")