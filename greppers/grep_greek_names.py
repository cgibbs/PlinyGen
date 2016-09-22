import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from bs4 import BeautifulSoup
import urllib2
import re

wiki = "http://nameberry.com/baby-names/167/Greek-Names"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

table = soup.find_all("li")

with open('..\\lists\\greek_names.txt', 'w') as f:
    for cells in table:
        write_to_file = ""
        for i in cells.strings:
            write_to_file += i.strip()
        write_to_file += "\n"
        f.write(write_to_file.encode('utf-8'))
