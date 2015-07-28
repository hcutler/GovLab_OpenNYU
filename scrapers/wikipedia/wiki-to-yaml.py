import urllib
from urllib2 import urlopen
import urllib2
import time
import wikipedia
from bs4 import BeautifulSoup
import yaml
import json
import sys
import encodings
from encodings import aliases
from unidecode import unidecode
# import pywikibot
# from pywikibot import pagegenerators
# import unicodedata as ud


# reload(sys)
# sys.setdefaultencoding("latin-1")

names = []
data = []

with open("people-list copy.yaml", "r") as yaml_file:
    entries = yaml_file.read().splitlines()
    
    for e in entries:
        if "---" in e:
            pass
        elif "people" in e:
            pass
        else:
            e.strip("- ")
            names.append(e) #append names to list

#create dictionary to store whether source exists for the person
val_keys = sources = ["Wikipedia", "Center for Data Science NYU"] #add to this as run each scraper
source_dict = dict(zip(val_keys, [False]*len(val_keys))) #set all values as false

all_d = []
i = 0
j = 0
numwiki = 0
for n in names[0:10]:
    d = {n: source_dict}
    all_d.append(d)

    #print all_d  # e.g. {Paul Glimcher : {"Wikipedia": False, "Center for Data Science NYU": False}}
    try:    
        # site = pywikibot.Site()
        # page = pywikibot.Page(site, n)
        # text = page.text
        # print text
        # cat = pywikibot.Category(site,'Category:Living people')
        # gen = pagegenerators.CategorizedPageGenerator(cat)
        # for page in gen:
        #   #Do something with the page object, for example:
        #   text = page.text

        title = wikipedia.page(n)
        pageurl = title.url
        summary = title.summary
        categs = title.categories
        outlinks = title.links
        sections = title.sections
        refs = title.references
        content = title.content
        # imageurl = title.images
        #set wikipedia value in dictionary to true
        str1 = "New York University"
        str2 = "NYU"
        if (str1 or str1.lower() or str2 or str2.lower) not in content:
            pass
        else:
            data.append({'summary': summary, 'url': pageurl ,
            	'categories': categs, 'outlinks': outlinks,'sections': sections,
            	'references': refs})  #'content': content, 'imageurl': imageurl} 'title': str(title)
            data.sort
            numwiki += 1

    # source_dict.update({"Wikipedia":True})
    #     i += 1

    except wikipedia.exceptions.DisambiguationError as e: #if reach this, they aren't on wikipedia
        #print e.options 
        j += 0
        pass
    except wikipedia.exceptions.PageError as pe:
        pass

# def remove_non_ascii_1(text):
#     # return ''.join([i if ord(i) < 128 else ' ' for i in text])
#     # data = remove_non_ascii_1(str(data))
#     try:
#     # if the title is a unicode string, normalize it
#         text = unicodedata.normalize('NFKD', title).encode('ascii','ignore')
#     except TypeError:
#     # if it was not a unicode string => OK, do nothing
#         pass

with open('wiki-data.yaml', 'w') as outfile:
    # remove_non_ascii_1(data)
    outfile.write( yaml.safe_dump(data,encoding='utf-8',default_flow_style=False,allow_unicode=True))

print "num wiki: " + str(numwiki)





########
        # data.append({'pageurl': str(pageurl), 'title': title, 'url': 'http://en.wikipedia.org/wiki/' + n, 'summary': str(summary),
        # 'categories': str(categs), 'outlinks': str(outlinks),'sections': str(sections),
        # 'references': refs,'imageurl': imageurl}) #'content': content, 

# data = str(data).decode("utf-8").replace(u"\u2022", " ").encode("utf-8").split(" ")

# def remove_non_ascii_1(text):
#     return ''.join([i if ord(i) < 128 else ' ' for i in text])
    # data = remove_non_ascii_1(str(data))
