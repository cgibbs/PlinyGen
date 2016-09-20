import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from bs4 import BeautifulSoup
import urllib2
import re

wiki = "http://www.healthline.com/health/skin-disorders"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

h3s = soup.find_all("h3", { "class" : "hl-content-listing-title-mobile" })

with open('..\\lists\\skin_disorders.txt', 'w') as f:
    for h3 in h3s:
        write_to_file = ""
        for i in h3.strings:
            write_to_file += i
        f.write(write_to_file.encode('utf-8') + "\n")
