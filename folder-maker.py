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
        
        #remove header and footers from list
        if "---" in e:
        	names.remove(e)
        if "people" in e:
        	names.remove(e)

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
		# if "people" in n:
		# 	pass
		# else:
		n.replace("\n", "")
		filename = path + '/' + n + '.yaml'
		open(filename, 'a').close()

create_folders("people-profiles")



# dirpath = 'S. R. Srinivasa Varadhan'
# filename = dirpath + '/S. R. Srinivasa Varadhan.yaml'
# filename = 'S. R. Srinivasa Varadhan/S. R. Srinivasa Varadhan.yaml'