#Import Modules

from bs4 import BeautifulSoup
import requests
import re

#Get the Data using URL

url = "https://www.imdb.com/chart/top"

#Get the page data

page = requests.get(url)
page.content

#parse the data
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#Regex to find particular class
tag = soup.find('div', class_ = re.compile(r'head+'))
print(tag)
print(tag.text)

#Using Regular Expression
print(re.findall(r'<title>(.*?)</title>', page.text))
print(re.findall(r'(<title>(.*?)</title>)', page.text))
