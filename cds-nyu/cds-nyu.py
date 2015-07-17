import urllib2
import time
from bs4 import BeautifulSoup

#get contents of CDS-NYU page
URL = "http://cds.nyu.edu/people/"
html_doc = urllib2.urlopen(URL).read()
soup = BeautifulSoup(html_doc)

# get list of all people
people = soup.find_all('h3')
i = 0
for person in people:
    print person.text
        lname = person.text.split(' ', 1)[1]
    print lname
    print person.text
    i += 1
print '# of faculty: ' + str(i)

contents = soup.find_all('h3', attrs={"class": "accent"})

# get and print NAME, EXPERTISE, TITLE of faculty member
people = []
for item in contents:
    name = item.text
    expertise = item.parent.parent.find('div', attrs={'class':'meta-info'}).text
    title = item.parent.find('h6').text
    people.append({'name':name,'title':title, 'expertise':expertise})

for p in people:
    print p