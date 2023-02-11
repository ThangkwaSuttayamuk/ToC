#Import Modules

from bs4 import BeautifulSoup
import requests
import re

#Get the Data using URL

url = "https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%89%E0%B8%B0%E0%B9%80%E0%B8%8A%E0%B8%B4%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%A3%E0%B8%B2"

#Get the page data

page = requests.get(url)
page.content

#parse the data
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find_all('li')
content = str(content)
#content = str(content)
#print(soup.prettify())

#re_titles = r'">วัด(.*?)</a>'
re_titles = r'">วัด(.*?)</a>'

titles_list = re.findall(re_titles, content)
print(titles_list)
#Regex to find particular class
with open("output.txt", "w", encoding='utf-8') as f:
   for title in titles_list:
       f.write( "วัด" + title + "\n")
