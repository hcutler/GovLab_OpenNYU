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

#parse local html
soup = BeautifulSoup(local_html)

# def get_name():
#     people = soup.find_all('h3')
#     i = 0

#     for person in people[0:2]:
#         fullname = person.text
#         print fullname
#         # print person.text
#         # lname = person.text.split(' ', 2)[2]
#         # print lname
#         i +=1


#get contents
contents = soup.find_all('h3', attrs={"class": "accent"})

# get names of all faculty
def get_name():
    i = 0
    for i in range(0,len(contents)):
        # for item in contents[0:2]:
        fullname = contents[i].text
        print fullname
        i+=1


def get_titles():
    titles = item.parent.parent.find('h6').text
    titles.split('; ')     # split titles
    print '\nTitles:'
    print titles


def get_expertise():
    pass


def get_data():
    for item in contents:
        get_name()
        get_titles()
        get_expertise()


# get and print NAME, EXPERTISE, TITLE(S) of faculty member
people = []




# for item in contents[0:2]:
#     fullname = item.text
#     expertise = item.parent.parent.find('div', attrs={'class':'meta-info'}).text
#     titles = item.parent.parent.find('h6').text

#     def split_titles():
#         titles.split('; ')
#         print titles

#     print '\nTitles:'
#     split_titles()

#     # print '\n' + str(i) + ') \n' + fullname + '\n' + expertise + '\n'
#     # i += 1

#     # title = item.parent.parent.find('h6').text #split further into individual titles!!
#     # people.append({'name': name,'title(s)': title, 'expertise': expertise})

# for p in people:
#     print p



