#!/usr/bin/env python
# coding: utf-8

import urllib.request
from bs4 import BeautifulSoup

url = 'https://minkabu.jp'
req = urllib.request.Request(url)
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")
nikkei = soup.find('h3', class_='fwn')
average = soup.find('div', class_='fsn fwb')
preday = soup.find('td', class_='tac wsnw vamd').find('div', class_='wsnw')
print('%s is %s %s'%(nikkei.text, average.text, preday.text.strip()))

url = 'https://minkabu.jp/stock/8750'
req = urllib.request.Request(url)
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")

# 株価
topics = soup.find('div', class_='stock_price')
dec = soup.find('div', class_='stock_price').find('span',class_='decimal')
unit = soup.find('div', class_='stock_price').find('span',class_='stock_price_unit')
price="8750 stock price is %s%s%s"%(topics.contents[0].strip(),dec.text,unit.text)

# 前日比
diff = soup.find('span', class_='stock_price_diff')
price_diff = "%s"%diff.text.strip()

print(price,price_diff)
