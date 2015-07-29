import urllib
from urllib2 import urlopen
import time
from bs4 import BeautifulSoup
import yaml
import os
import sys

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
            continue
    print names