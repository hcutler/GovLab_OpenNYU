import urllib
from urllib2 import urlopen
import urllib2
import time
import wikipedia
from bs4 import BeautifulSoup
import yaml
import json
import sys

#open/read all data files
with open("wiki-data.yaml", "r") as yaml_file:
    wiki_entries = yaml_file.read()

#write data to one big file
with open('master-raw.yaml', 'w') as outfile:
	outfile.write( yaml.dump(wiki_entries, default_flow_style=False) )

with open("cds-data.yaml", "r") as yaml_file:
    cds_entries = yaml_file.read()
    
#write data to one big file
with open('master-raw.yaml', 'a') as outfile:
    outfile.write( yaml.dump(cds_entries, default_flow_style=False) )
    
print "finished"