import urllib2
import time
import wikipedia
from bs4 import BeautifulSoup

#prompt user to enter topic
topic = raw_input("\nPlease enter a topic: \n")

#fetch page for topic
url = urllib.urlopen("http://en.wikipedia.org/wiki/" + topic)

print("Fetching the Wikipedia page contents for '" + topic + "'... \n")

#store contents
page = wikipedia.page(topic)
summary = wikipedia.summary(topic)


# print page[1]
# print("Summary: \n") + summary + '\n'

# fix this so formatting is correct when looks for the stuff -- need to do linking things
# print url.read()




# #translate into chinese
# lang = wikipedia.set_lang("zh")
# chinese = wikipedia.summary(topic, sentences=1)
# print chinese