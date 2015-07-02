import datetime
import urllib
import time
from bs4 import BeautifulSoup
from linkedin import linkedin
from oauthlib import *
from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)

API_KEY = '77p81cbtycxb3s' #CONSUMER_KEY
API_SECRET = 'NllPQrOxRDcXUGK6' #CONSUMER_SECRET

#USER_TOKEN (oauth_token)
#USER_SECRET (oauth_secret)
RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
# print authentication.authorization_url  # open this url on your browser

# Pass it in to the app...
application = linkedin.LinkedInApplication(authentication)

# Use the app....
# g = application.get_profile()
g = application.r_basicprofile()
print 'successful\n'
print g



# r_basicprofile