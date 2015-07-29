import urllib
from urllib2 import urlopen
import time
from bs4 import BeautifulSoup
import yaml
import os
import sys

# read in master_raw

# loop through list of names - start with single person

#be smart about how the scraper goes about getting informaiton to populate the profiles
#run kNN BEFORE.
#then go through and that's how it scrapes stuff
#academic
#non-academic

people = []
entries = []

with open("people-list.yaml", "r") as yaml_file:
	people = yaml_file.read().split('\n- ')
	# for p in people:
	# 	print p

with open("master-raw.yaml", "r") as yaml_file:
	entries =  yaml.load(yaml_file)
	# for e in entries:
	# 	for k, v in e.items():
	# 		print (k,v)
		# print e
	# entries = yaml_file.read()

def get_name():
	i = 0
	for e in entries:
		for k,v in e.items():
			if "fullname" in k:
				if p == v:
					fullname = v
					print (k,v)
	print "name: " + fullname

	# def get_position():
	# 	position = ""
	# 	for p in people[1:2]:

def get_title(name):
	for p in people:
		for e in entries:
			for k,v in e.items():
				if ("titles" in k) and (p == name):
					print (k,v)

	# print "title: " + title

get_name()
# get_title()

	# def get_dept():


	# def get_school(): 
	# 	pass

	# def get_institution():
	# 	pass

def get_location():
	if "Poly" in institution:
		city = "Brooklyn"
	else:
		city = "New York"
	state = "NY"

def get_contact_info():
	pass
	# get_phone()
	# get_email()
	# get_twitter()
	# get_linkedin()

def make_profile_file():
	pass

