import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from bs4 import BeautifulSoup
import urllib2
import re

wiki = "https://en.wikipedia.org/wiki/List_of_rivers_of_Greece"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

table = soup.find_all("li")

with open('..\\lists\\rivers.txt', 'w') as f:
    for cells in table:
        write_to_file = ""
        for i in cells.strings:
            write_to_file += i
        if '(' in write_to_file:
            write_to_file = write_to_file[0:write_to_file.find('(')].strip()
        if ',' in write_to_file:
            write_to_file = write_to_file[0:write_to_file.find(',')].strip()
        if '/' in write_to_file:
            write_to_file = write_to_file[0:write_to_file.find('/')].strip()
        write_to_file += "\n"
        f.write(write_to_file.encode('utf-8'))
