import requests
from bs4 import BeautifulSoup

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