import urllib2
import time
from bs4 import BeautifulSoup
from yaml import load, Loader


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

#######
# # get list of all people
# people = soup.find_all('h3')
# i = 0
# for person in people[0:2]:
#     fullname = person.text
#     print fullname
#     # print person.text
#     # lname = person.text.split(' ', 2)[2]
#     # print lname
#     i +=1
# print '# of faculty: ' + str(i)
#######

contents = soup.find_all('h3', attrs={"class": "accent"})

# get and print NAME, EXPERTISE, TITLE of faculty member
people = []

for item in contents[0:2]:
    name = item.text
    expertise = item.parent.parent.find('div', attrs={'class':'meta-info'}).text
    title = item.parent.parent.find('h6').text #parse this further!! (posit / dept / school)
    people.append({'name': name,'title(s)': title, 'expertise': expertise})

for p in people:
    print p