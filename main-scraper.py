import urllib2
import time
from bs4 import BeautifulSoup

print('Welcome to the ExpertNet tool. \n')

topic = raw_input("Enter a topic: ")

print("Let me try to understand the kind of expertise you are looking for" + '\n')
print("In your opinion, are you most likely to find information about '" + topic + "' on: " + '\n')
print("      1.  Social media site (Facebook, Twitter, Instagram) \n")
print("      2.  Wikipedia \n")
print("      3.  Website of an academic institution \n")
print("      4.  Research journal or publication\n")
print("(Type the NUMBER of your choice and press ENTER)")

# url = urllib.urlopen("http://en.wikipedia.org/wiki/Beth_Simone_Noveck")
# print url.read()