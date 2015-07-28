import urllib
from urllib2 import urlopen
import urllib2
import time
import wikipedia
from bs4 import BeautifulSoup
import yaml
import json
import sys



data = []
# read wiki write wiki read cds append cds -- open/read all data files
wiki_entries = []
cds_entries = []

with open("wiki-data.yaml", "r") as yaml_file:
    # wiki= yaml_file.read()
    wiki = yaml.load(yaml_file)

# with open('master-raw.yaml', 'w') as outfile:
    # outfile.write( yaml.dump(wiki_entries, default_flow_style=False) )
# 	# for d in data:
# 	outfile.write( yaml.safe_dump(str(data1), encoding='utf-8',default_flow_style=False, allow_unicode=True) )

with open("cds-data.yaml", "r") as yaml_file:
    # cds = yaml_file.read()
    cds = yaml.load(yaml_file)

data = wiki + cds

with open('master-raw.yaml', 'w') as outfile:
	outfile.write( yaml.safe_dump(data, encoding='utf-8',default_flow_style=False, allow_unicode=True) )
	# outfile.write( yaml.safe_dump(cds_entries, encoding='utf-8',default_flow_style=False, allow_unicode=True) )






