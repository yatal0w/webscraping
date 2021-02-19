#!/usr/bin/env python 
import urllib.request
from bs4 import BeautifulSoup
import datetime

url = 'https://cybersecurity-jp.com/news'
req = urllib.request.Request(url)
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")
topics = soup.find_all('h2',class_='post-title')
dates = soup.find_all('li',class_='date')
lists = []
for da in dates:
  lists.append(da.get('datetime'))

today = datetime.date.today()
td = today.strftime('%Y-%m-%d')

i = 0
for topic in topics:
  ldate = lists[i]
  ld = ldate[0:10]
  if td == ld: 
    title = topic.find('a')
    print(title.string)
    print(lists[i])
    print(title.get('href'))
    print()
  i=i+1

url = 'https://thebridge.jp'
req = urllib.request.Request(url)
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")
topics = soup.find_all('h1',class_='entry-title')
dates = soup.find_all('time',class_='entry-date')
lists = []
for dt in dates:
  lists.append(dt.string)

td = today.strftime('%Y.%m.%d')
i = 0
for topic in topics:
  ldate = lists[i]
  ld = ldate[0:10]
  if td == ld:
    title = topic.find('a')
    print(title.string)
    print(lists[i])
    print(title.get('href'))
    print()
  i=i+1

