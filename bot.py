import praw
import OAuth2Util
import random
import urllib.request
from bs4 import BeautifulSoup

''' Variables '''

SUBREDDIT = 'RequestABot'

''' Code '''

r = praw.Reddit("Random Link Poster by /u/WildMonkeys") # UserAgent
o = OAuth2Util.OAuth2Util(r)

linksFile = open('links.txt', 'r') # Read-only
links = []

for link in linksFile:
	links.append(link)

if links != None:
	randomLink = random.choice(links)
	URLObject = urllib.request.urlopen(randomLink)
	html = BeautifulSoup(URLObject.read(), "html.parser")
	title = html.find('title').contents[0]
	
	r.submit(SUBREDDIT, title, url=randomLink, resubmit=True)
	
else:
	print('No links in the .txt file!')
	
print('Done')