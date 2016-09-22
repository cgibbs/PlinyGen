import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from bs4 import BeautifulSoup
import urllib2
import re

wiki = "https://en.wikipedia.org/wiki/List_of_Greek_mythological_figures"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

tables = soup.find_all("table", { "class" : "wikitable" })

with open('..\\lists\\greek_mythos.txt', 'w') as f:
    for table in tables:
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            write_to_file = ""
            if len(cells) < 3:
                continue
            for i in cells[1].strings:
                write_to_file += i
            write_to_file += ", "
            for i in cells[2].strings:
                write_to_file += i
            if '.' in write_to_file:
                write_to_file = write_to_file[0:write_to_file.find('.')].strip()
            write_to_file += "\n"
            f.write(write_to_file.encode('utf-8'))
