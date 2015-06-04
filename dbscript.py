from lxml import etree
import lxml
import os
from os.path import join, getsize
from xml.etree.ElementTree import ElementTree
import csv
from csv import DictWriter


peoplerows = []
grantrows = []
grantforrows = []

#parse XML files to extract data
for root, dirs, files in os.walk('NSF_data/'):
	for filename in files[0:1]:
		if filename.endswith('.xml'):
			fullpath = os.path.join(root, filename)

			try:
				f = open(fullpath)
				print fullpath
				doc = etree.parse(f)

				title = doc.xpath('//AwardTitle')
				effdate = doc.xpath('//AwardEffectiveDate')
				expirdate = doc.xpath('//AwardExpirationDate')
				amount = doc.xpath('//AwardAmount')
				directorate = doc.xpath('//Organization/Directorate/LongName')
				division = doc.xpath('//Organization/Division/LongName')
				abstract = doc.xpath('//AbstractNarration')
				awardid = doc.xpath('//AwardID')
				
				first = doc.xpath('//Investigator/FirstName')
				last = doc.xpath('//Investigator/LastName')
				# investigatorname = first[0].text + " " + last[0].text
				investors = doc.xpath('//Investigator')
				for investor in investigators:
					fname = 
				investigatoremail = doc.xpath('//Investigator/EmailAddress')
				institution = doc.xpath('//Institution/Name')

				#investigators messed up

				peopleheaders = ['PersonID', 'FirstName', 'LastName', 'Email', 'Institution']

				grantheaders = ['PersonID', 'Title', 'EffDate','ExpirDate',
								'Amount', 'Directorate', 'Division' , 'Abstract' , 'AwardID']

				grantforheaders = ['PersonID', 'AwardID']


				peoplerows.append({'PersonID': investigatoremail[0].text, 'FirstName': first[0].text,
						'LastName': last[0].text, 'Email': investigatoremail[0].text,
						'Institution': institution[0].text})

				grantrows.append({'PersonID': investigatoremail[0].text, 'Title': title[0].text, 'EffDate': effdate[0].text,
						'ExpirDate': expirdate[0].text, 'Amount': amount[0].text, 'Directorate': directorate[0].text,
						'Division': division[0].text, 'Abstract': abstract[0].text, 'AwardID': awardid[0].text})

				grantforrows.append({'PersonID': investigatoremail[0].text, 'AwardID': awardid[0].text})
			
			except Exception, e :
				print "Error with file %s" % fullpath	
				print e

#generate 3 csv files
with open('people.csv', 'w') as f:
	f_csv = csv.DictWriter(f, peopleheaders)
	f_csv.writeheader()
	f_csv.writerows(peoplerows)

with open('grants.csv', 'w') as f:
	f_csv = csv.DictWriter(f, grantheaders)
	f_csv.writeheader()
	f_csv.writerows(grantrows)

with open('grantfor.csv', 'w') as f:
	f_csv = csv.DictWriter(f, grantforheaders)
	f_csv.writeheader()
	f_csv.writerows(grantforrows)


"""
TABLE people
id varchar(20), 
first_name text,
last_name text,
email text,

TABLE grant
id varchar(20),
person_id ....
title text
eff_date date
expir_date date
amount int 
directorate text
division text
abstract text
awardid text

TABLE grant_for
grant_id
person_id

"""