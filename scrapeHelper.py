import requests
from bs4 import BeautifulSoup

''' Scraping the correct weeks'''

def getFirstYear(url='http://rotoguru1.com/cgi-bin/fyday.pl'):
    # TODO: Actually grab this from the webpage
    return 2011

def getLastYear(url='http://rotoguru1.com/cgi-bin/fyday.pl'):
    # TODO: Actually grab this from the webpage
    return 2017

def getFirstWeek():
    return 1

def getLastWeek(year):
    # TODO: Actually grab this from the webpage
    if (year == 2017):
        return 7
    else:
        return 17

''' Grabbing the fields into the proper fields '''

# Takes all data which is found in a <pre> tag in this case
def grabData(soup):
    return soup.find_all('pre')[0].get_text()

# Iterates through rowified data and places it into lists
def appendValues(separatedValues, allLists):
    numValues = len(separatedValues)
    for eachValue in range(0,numValues):
        allLists[eachValue].append(separatedValues[eachValue])


''' Higher level functions '''

# Tokenizes data and appends it to appropriate global lists
def appendData(delimitedData,allLists):
    separatedRows = delimitedData.split('\n')
    numRows = len(separatedRows) - 1

    for eachRow in range(1,numRows):

        # Separates each value, which was delimited by a semicolon before
        separatedValues = separatedRows[eachRow].split(';')

        #Append each value to its appropriate list
        appendValues(separatedValues,allLists)