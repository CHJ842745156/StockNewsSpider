# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:54:57 2020

@author: CHJ
"""

import requests as req
from bs4 import BeautifulSoup

url = 'https://www.toutiao.com/c/user/token/MS4wLjABAAAA56eGL40AT6T7eLJ7ir3rhX74Fa6LtzNWkfcq2jcXAek/'

HtmlStr = req.get(url)

soup = BeautifulSoup(HtmlStr,'lxml')
#print(soup.title)
#print(soup.p['class'])
#print(soup.find_all('a'))
#print(soup)
print(soup.prettify())

print(soup)