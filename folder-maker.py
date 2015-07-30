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
    for n in names:
        n.replace("\n", "")
        filename = path + '/' + n + '.yaml'
        populate_files(filename)

def populate_files(fname):
    with open(fname, 'w') as outfile:
        outfile.write("---" + '\n' + "fullname:" + '\n')
        outfile.write("firstname:" + '\n')
        outfile.write("lastname:" + '\n')
        outfile.write("position:" + '\n')
        outfile.write("department:" + '\n')
        outfile.write("school:" + '\n')
        outfile.write("institution:" + '\n')
        outfile.write("gender:" + '\n')
        outfile.write('\n' + "location:" + '\n')
        outfile.write("    " + "city:" + '\n')
        outfile.write("    " + "state:" + '\n')
        outfile.write('\n' + "contact:" + '\n')
        outfile.write("    " + "phone:" + '\n')
        outfile.write("    " + "email:" + '\n')
        outfile.write("    " + "website:" + '\n')
        outfile.write("    " + "twitter:" + '\n')
        outfile.write("    " + "linkedin:" + '\n')
        outfile.write("    " + "facebook:" + '\n')
        outfile.write("    " + "github:" + '\n')
        outfile.write('\n' + "skills:" + '\n' + "    - n/a")
        outfile.write('\n' + "sources:" + '\n' + "    - http://cds.nyu.edu/people/")
        outfile.write('\n' + '...')    
            # outfile.write( yaml.safe_dump(person_list_unique,encoding='utf-8',default_flow_style=False,allow_unicode=True))
        # open(filename, 'a').close() # what does this do??

create_folders("people-profiles")



# dirpath = 'S. R. Srinivasa Varadhan'
# filename = dirpath + '/S. R. Srinivasa Varadhan.yaml'
# filename = 'S. R. Srinivasa Varadhan/S. R. Srinivasa Varadhan.yaml'