import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

'''
currWeek = 5

for weekNo in range(1,currWeek):
    url = 'http://rotoguru1.com/cgi-bin/fyday.pl?week=' + currWeek + '&game=fd&scsv=1'
    page = requests.get(url)
'''

# The URL we will be reading in our Fanduel Data from
url = 'http://rotoguru1.com/cgi-bin/fyday.pl?week=5&game=fd&scsv=1'

# Pulls down page
page = requests.get(url)

# Grabs content
soup = BeautifulSoup(page.content, 'html.parser')

# Takes all data which is found in a <pre> tag in this case
actualData = soup.find_all('pre')[0].get_text()

# Separates the data by semi-colons and stores in a list
myList = actualData.split(';')
print myList[:100]
print type(myList)


