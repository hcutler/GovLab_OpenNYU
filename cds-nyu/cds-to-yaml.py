import urllib2
import time
from bs4 import BeautifulSoup
#from yaml import load, Loader

import yaml
import json

#get contents of CDS-NYU page
URL = "http://cds.nyu.edu/people/"
html_doc = urllib2.urlopen(URL).read()
# soup = BeautifulSoup(html_doc)

#save copy of HTML contents locally
with open("cds-nyu.html", "w") as html_file:
    html_file.write(html_doc)

with open("cds-nyu.html", "r") as html_file:
    local_html = html_file.read()

soup = BeautifulSoup(local_html)

contents = soup.find_all('h3', attrs={"class": "accent"})

# get and print NAME, EXPERTISE, TITLE, LINK of faculty member
people = []
# people = dict()

def get_person_data():
	for item in contents:
	    fullname = item.text
	    expertise = item.parent.parent.find('div', attrs={'class':'meta-info'}).text
	    
	    #get titles
	    titles = item.parent.parent.find('h6').text
	    titles.split('; ')


	    #get link
	    linkblock = item.parent.prettify()  # extract codeblock with link
	    link = linkblock.split("=")[1]	# extract link
	    namelink = link.split(" ")[0] #slice off extra stuff
	
	    people.append({'titles': titles, 'fullname': fullname, 'expertise': expertise, 'namelink': namelink})


	# only returning last value... this is why: http://stackoverflow.com/questions/20398242/python-list-iteration-only-returns-last-value

get_person_data()

# #print as JSON
# print json.dumps(people, sort_keys=True, indent=2)


with open('cds-data.yaml', 'w') as outfile:
	outfile.write( yaml.dump(people, default_flow_style=False) )



#####


	   # print namelink
	    # nl = namelink.find_all('href')
	    # ('a', attrs={"href":'meta-info'})

	    #namelink = item.find('a', attrs={'href':'meta-info'}).text
	    # people.append({'name': name, 'expertise': expertise})
	    #people.append({'name': name,'title(s)': titles, 'expertise': expertise})
	    #print namelink

	# for p in people:
	# 	print p