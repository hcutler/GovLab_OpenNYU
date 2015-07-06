import datetime
import urllib
import time
from bs4 import BeautifulSoup
from linkedin import linkedin
from oauthlib import *
from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)
from linkedin import server


# docs: http://ozgur.github.io/python-linkedin/

API_KEY = '77p81cbtycxb3s' #CONSUMER_KEY
API_SECRET = 'NllPQrOxRDcXUGK6' #CONSUMER_SECRET

#USER_TOKEN (oauth_token)
#USER_SECRET (oauth_secret)
RETURN_URL = 'http://localhost:8080'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url  # open this url on your browser
application = linkedin.LinkedInApplication(authentication) # Pass it in to the app...


authentication.authorization_code = 'AQTXrv3Pe1iWS0EQvLg0NJA8ju_XuiadXACqHennhWih7iRyDSzAm5jaf3R7I8'
authentication.get_access_token()


application = server.quick_api(KEY, SECRET)

# # Use the app....
# gp = application.get_profile()


gp = application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
# application.get_connections(selectors=['headline', 'first-name', 'last-name'], params={'start':10, 'count':5})
# application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})
# application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'apple microsoft'})


# g = application.r_basicprofile()
print gp
