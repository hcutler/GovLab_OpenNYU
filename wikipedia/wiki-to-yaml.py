import urllib
import time
import wikipedia #https://wikipedia.readthedocs.org/en/latest/code.html
from bs4 import BeautifulSoup
import yaml
import json


#create list of names
queries = []
with open("people-list-copy.yaml", "r") as yaml_file:
    queries.append(str(yaml_file.read()))
    
for q in queries:
	url = urllib.urlopen("http://en.wikipedia.org/wiki/" + q)
	print url

	#save contents of all pages

#feed names as queries to wikipedia



# for q in queries:
#feed people into wikipedia as queries. save data to yaml file.
# topic = raw_input(

# url = urllib.urlopen("http://en.wikipedia.org/wiki/" + topic)

#get list of faculty (all NYU? just CDS?)
#loop through list
#query wikipedia for all people on list
#if a page exists for a given faculty member, download contents of the page
# 
#get contents of wiki pages for all faculty if they exist