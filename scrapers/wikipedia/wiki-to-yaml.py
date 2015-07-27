import urllib
from urllib2 import urlopen
import urllib2
import time
import wikipedia
from bs4 import BeautifulSoup
import yaml
import json
import sys

names = []
data = []

with open("people-list copy.yaml", "r") as yaml_file:
    entries = yaml_file.read().splitlines()
    
    num = 0
    for e in entries:
        names.append(e) #append names to list
#create dictionary to store whether source exists for the person
        num += 1
#     print num

val_keys = sources = ["Wikipedia", "Center for Data Science NYU"] #add to this as run each scraper
source_dict = dict(zip(val_keys, [False]*len(val_keys))) #set all values as false

all_d = []
i = 0
j = 0
for n in names[0:3]:
    d = {n: source_dict}
    all_d.append(d)
    #print all_d  # e.g. {Paul Glimcher : {"Wikipedia": False, "Center for Data Science NYU": False}}
    try:
        pageurl = urllib.urlopen("http://en.wikipedia.org/wiki/" + n)        
        title = wikipedia.page(n)
        summary = title.summary
        categs = title.categories
        outlinks = title.links
        sections = title.sections
        refs = title.references
        # content = title.content
        imageurl = title.images
        # print p + " has wiki"
        #set wikipedia value in dictionary to true
        source_dict.update({"Wikipedia":True})
        i += 1
        # data.append({'pageurl': str(pageurl), 'title': title, 'url': 'http://en.wikipedia.org/wiki/' + n, 'summary': str(summary),
        # 'categories': str(categs), 'outlinks': str(outlinks),'sections': str(sections),
        # 'references': refs,'imageurl': imageurl}) #'content': content, 
        
        data.append({'title': title, 'summary': summary, 'url': 'http://en.wikipedia.org/wiki/' + n,
        	'categories': categs, 'outlinks': outlinks,'sections': sections,
        	'references': refs, 'imageurl': imageurl})  #'content': content,

    except wikipedia.exceptions.DisambiguationError as e: #if reach this, they aren't on wikipedia
        #print e.options 
#         print p + " no wiki"
        j += 0
        pass
    except wikipedia.exceptions.PageError as pe:
#       print p + " no wiki"
        pass

with open(u'wiki-data.yaml', 'w') as outfile:
	outfile.write( yaml.dump(data, encoding='utf-8',default_flow_style=False, allow_unicode=True) )
# 	outfile.write( yaml.dump(data, encoding='utf-16', default_flow_style=False, allow_unicode=False) )
# yaml.dump(data, file(u'wiki-data.yaml','w'), default_flow_style=False, allow_unicode=True)

# yaml.safe_dump(data, file('wiki-data.yaml','w'), encoding='utf-8',default_flow_style=False, allow_unicode=True)

# .safe_dump(person_list_unique, encoding='utf-8', default_flow_style=False, allow_unicode=True) )

	# print "finished!"



