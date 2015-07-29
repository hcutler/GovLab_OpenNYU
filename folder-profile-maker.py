import urllib
from urllib2 import urlopen
import time
from bs4 import BeautifulSoup
import yaml
import os
import sys

names = []
with open("people-list.yaml", "r") as yaml_file:
    entries = yaml_file.read().splitlines()
    num = 0
    for e in entries:
        names.append(e.replace("- ", ""))
        
        if "people" in e:
        	names.remove(e)
        elif "---" in e:
        	names.remove(e)
        else:
        	continue

def create_folders(dirname, path=os.getcwd()): # how to put the folder in a different (parent) directory?
    dirpath = os.path.join(path, dirname)
    try:
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
            create_files(dirname)
            # open(dirpath + ".yaml", 'a').close()
    except OSError as error:
        print error

def create_files(dirname):
	path = dirname
	for n in names[0:82]:
		# if "---" in n:
		# 	pass
		# else:
		n.replace("\n", "")
		filename = path + '/' + n + '.yaml'
		open(filename, 'a').close() # what does this do??

create_folders("people-profilesTEST")


#generate profiles



def get_name():
    pass

def get_position():
    pass

def get_dept():
    pass

def get_school(): 
    pass

def get_institution():
    pass

def get_location():
    if "Poly" in institution:
        city = "Brooklyn"
    else:
        city = "New York"
    state = "NY"

def get_contact_info():
    pass

def make_profile_file():
    pass




#######
# dirpath = 'S. R. Srinivasa Varadhan'
# filename = dirpath + '/S. R. Srinivasa Varadhan.yaml'
# filename = 'S. R. Srinivasa Varadhan/S. R. Srinivasa Varadhan.yaml'