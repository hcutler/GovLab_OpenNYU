import urllib2
import time
from bs4 import BeautifulSoup
from yaml import load, Loader
import yaml


#get contents of CDS-NYU page
URL = "http://cds.nyu.edu/people/"
html_doc = urllib2.urlopen(URL).read()
soup = BeautifulSoup(html_doc)

#save copy of HTML contents locally
with open("cds-nyu.html", "w") as html_file:
    html_file.write(html_doc)

with open("cds-nyu.html", "r") as html_file:
    local_html = html_file.read()


people = soup.find_all('h3')
person_list = []
person_list_unique = [] #generate set to remove duplicates

# i = 0
for person in people:
    fullname = person.text.encode('utf-8') # get rid of '!!python/unicode' 's
    person_list.append(fullname)

    for p in person_list:
    	if p not in person_list_unique:
    		person_list_unique.append(p)
    		# i +=1

# print '# of faculty: ' + str(i)

# with open("people-list.txt", "w") as txt_file:
# 	txt_file.write(str(person_list))

with open('people-list.yaml', 'w') as outfile:
	outfile.write( yaml.dump(person_list_unique, default_flow_style=False) )





