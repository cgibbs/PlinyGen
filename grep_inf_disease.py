import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from bs4 import BeautifulSoup
import urllib2
import re

wiki = "https://en.wikipedia.org/wiki/List_of_infectious_diseases"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

table = soup.find("table", { "class" : "wiki table sortable" })

with open('./inf_diseases.txt', 'w') as f:
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        write_to_file = ""
        for i in cells[0].strings:
            write_to_file += i
        write_to_file += "\n"
        f.write(write_to_file.encode('utf-8'))
