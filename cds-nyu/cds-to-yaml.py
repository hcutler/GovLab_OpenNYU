import urllib2
import time
from bs4 import BeautifulSoup
import yaml

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

# get and print NAME, EXPERTISE, TITLE of faculty member
people = []

def get_person_data():
	for item in contents[0:2]:
	    name = item.text
	    expertise = item.parent.parent.find('div', attrs={'class':'meta-info'}).text
	    
	    titles = item.parent.parent.find('h6').text #parse this further!! (posit / dept / school)
	    titles.split('; ')
	    link
	    people.append({'name': name,'title(s)': titles, 'expertise': expertise, 'link': ____})


get_person_data()

for p in people:
	print people

# with open('cds-data.yaml', 'w') as outfile:
#     # outfile.write( yaml.dump(data, default_flow_style=True) )
# 	outfile.write( yaml.dump(people, default_flow_style=True) )