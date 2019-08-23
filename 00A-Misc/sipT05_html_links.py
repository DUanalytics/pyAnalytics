# -*- coding: utf-8 -*-
#https://www.quora.com/How-do-I-extract-links-from-a-given-text-file-using-Python
#-----------------------------
#%
#https://hackingandslacking.com/scraping-urls-with-beautifulsoup-e794a555bb0f
from bs4 import BeautifulSoup, SoupStrainer
 
with open('data/hyperlink.txt','r') as f:
    for link in BeautifulSoup(f.read(), parse_only=SoupStrainer('a')): 
        if link.has_attr('href'): 
            print(link['href'])
            
            