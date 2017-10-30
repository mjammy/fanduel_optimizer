import requests
from bs4 import BeautifulSoup
from scrapeHelper import *
import pandas as pd
import numpy as np

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
page= requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Takes all data which is found in a <pre> tag in this case
actualData = soup.find_all('pre')[0].get_text()

# Separates the data by semi-colons and stores in a list
myList = actualData.split(';')
print myList[:100]
print type(myList)



