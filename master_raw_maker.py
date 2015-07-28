import urllib
from urllib2 import urlopen
import urllib2
import time
import wikipedia
from bs4 import BeautifulSoup
import yaml
import json
import sys

# cds = []
# # read wiki write wiki read cds append cds
# # open/read all data files
# wiki_entries = []
# cds_entries = []
# with open("wiki-data.yaml", "r") as yaml_file:
#     wiki_entries = yaml_file.read()

# # write data to one big file
# with open('master-raw.yaml', 'w') as outfile:
# 	# outfile.write( yaml.dump(wiki_entries, default_flow_style=False) )
#     outfile.write( yaml.safe_dump(wiki_entries, encoding='utf-8',default_flow_style=False, allow_unicode=True) )

# with open("cds-data.yaml", "r") as yaml_file:
#     cds_entries = yaml_file.read()
    
# #write data to one big file
# with open('master-raw.yaml', 'a') as outfile:
#     # outfile.write( yaml.dump(cds_entries, default_flow_style=False) )
#     outfile.write( yaml.safe_dump(cds_entries, encoding='utf-8',default_flow_style=False, allow_unicode=True) )
# print "finished"

data = []
# read wiki write wiki read cds append cds
# open/read all data files
wiki_entries = []
cds_entries = []
with open("wiki-data.yaml", "r") as yaml_file:
    wiki= yaml_file.read()
    wiki_entries.append(wiki)


with open("cds-data.yaml", "r") as yaml_file:
    cds = yaml_file.read()
    cds_entries.append(cds)

data = wiki_entries + cds_entries

# for d in data:
# 	print d

# # write data to one big file
# with open('master-raw.yaml', 'w') as outfile:
# 	# outfile.write( yaml.dump(wiki_entries, default_flow_style=False) )
#     for w in wiki_entries:
# 		outfile.write( yaml.safe_dump(w, encoding='utf-8',default_flow_style=False, allow_unicode=True) )

# # write data to one big file
# with open('master-raw.yaml', 'a') as outfile:
#     # outfile.write( yaml.dump(cds_entries, default_flow_style=False) )
# 	for c in cds_entries:
# 		outfile.write( yaml.safe_dump(c, encoding='utf-8',default_flow_style=False, allow_unicode=True) )
# print "finished"

with open('master-raw.yaml', 'w') as outfile:
    # outfile.write( yaml.dump(cds_entries, default_flow_style=False) )
	for d in data:
		outfile.write( yaml.safe_dump(d, encoding='utf-8',default_flow_style=False, allow_unicode=True) )

#read wiki store in list read cds append to list write list to yaml file
# #open/read all data files
# data = []
# with open("wiki-data.yaml", "r") as yaml_file:
# 	wiki_entries = yaml_file.read()

# with open("cds-data.yaml", "r") as yaml_file:
# 	cds_entries = yaml_file.read()
# 	data += cds_entries

# for d in data:
# 	data.split(" ")

# print data
#     wiki_entries.append(cds_entries)

# #     # write data to one big file
# with open('master-raw.yaml', 'w') as outfile:
# 	outfile.write( yaml.dump(wiki_entries, default_flow_style=False) )
    # for d in data:
    # 	d.replace("  \ ", " ")
    
#write data to one big file
# with open('master-raw.yaml', 'a') as outfile:
#     # outfile.write( yaml.dump(cds_entries, default_flow_style=False) )
#     outfile.write( yaml.safe_dump(cds_entries, encoding='utf-8',default_flow_style=False, allow_unicode=True) )
# print "finished"