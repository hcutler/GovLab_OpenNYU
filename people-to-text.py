import urllib
from urllib2 import urlopen
import time
from bs4 import BeautifulSoup
import yaml
import os
import sys
import encodings
from encodings import aliases
from unidecode import unidecode




names = []
with open("people-list.yaml", "r") as yaml_file:
    entries = yaml_file.read().splitlines()
    num = 0
    for e in entries:
        names.append(e.replace("- ", ""))
        
        if "people" in e:
        	names.remove(e)
        elif "---" in e:
        	names.remove(e)
        else:
            strnames = str(names).replace("',", ".yaml',")

with open("files.txt", 'w') as output_file:
    output_file.write(strnames.encode('utf-8'))

