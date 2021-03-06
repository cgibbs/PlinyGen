# coding=latin-1

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from bs4 import BeautifulSoup
import urllib2
import re

wiki = "https://en.wikipedia.org/wiki/List_of_plants_by_common_name"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

uls = soup.find_all("ul")

with open('..\\lists\\plants.txt', 'w') as f:
    for ul in uls:
        for item in ul.findAll("li"):
            write_to_file = ""
            for i in item.strings:
                write_to_file += i
            if len(write_to_file) < 4:
                continue
            if '–'.decode('utf-8') in write_to_file:
                write_to_file = write_to_file[0:write_to_file.find('–'.decode('utf-8'))].strip()
            f.write(write_to_file.encode('utf-8') + "\n")
