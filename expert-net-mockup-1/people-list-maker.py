import urllib2
import time
from bs4 import BeautifulSoup
from yaml import load, Loader
from unidecode import unidecode
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
    fullname = person.text.encode('utf-8') # remove '!!python/unicode' 's
    # # fullname.strip("!!python/str")

    # for char in person_list:
    # 	if char in "!!python/str":
    # 		fullname.replace(char,'')

    person_list.append(fullname)

    # for char in person_list:
    # 	if char in "!!python/str":
    # 		fullname.replace(char,'')

    for p in person_list:
		if p not in person_list_unique:
			person_list_unique.append(p)
    		# i +=1
# print person_list

with open('people-list.yaml', 'w') as outfile:
    outfile.write("---" + '\n' + "people:" + '\n')
    outfile.write( yaml.safe_dump(person_list_unique,encoding='utf-8',default_flow_style=False,allow_unicode=True))
    outfile.write("...")
	# generate files for each of these people in directory /profile-data/{p0,...,pn}
# yaml.safe_dump(person_list_unique, file('people-list.yaml','w'), encoding='utf-8', allow_unicode=True)

########
# print '# of faculty: ' + str(i)

# with open("people-list.txt", "w") as txt_file:
# 	txt_file.write(str(person_list))
########