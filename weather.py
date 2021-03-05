#!/usr/bin/env python 

import urllib.request
from bs4 import BeautifulSoup

url = 'https://tenki.jp/lite/forecast/3/17/4610/14130/'
req = urllib.request.Request(url)
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")
topics = soup.find_all('section',id='tomorrow_weather')

for topic in topics:
  # 日付
  tp = topic.find('h3')
  print(tp.text)
  # 最高気温
  max = topic.find('dt',class_='high-temp summary')
  max_temp = topic.find('dd',class_='high-temp temp')
  # 最低気温
  min = topic.find('dt',class_='low-temp summary')
  min_temp = topic.find('dd',class_='low-temp temp')
  print(max.text, max_temp.text, ' ', min.text, min_temp.text)
  print()
  # 降水確率
  print(topic.find_all('th',class_='precip-index')[1].text)
  times = topic.find_all('th',class_='time')
  ames = topic.find_all('td')
  for i in range(0,4,2):
    print(times[i].text,':',ames[i].text, ' ', times[i+1].text, ames[i+1].text)
  print()
  # 風
  winds = topic.find_all('dl',class_='wind-wave')
  for wind in winds:
    d = wind.find_all('dt')
    t = wind.find_all('dd')
    print(d[0].text,t[0].text)
    print(d[1].text,t[1].text)
  # 天気
  tenki = topic.find('img')
  print(tenki['src'])
