import requests
from bs4 import BeautifulSoup

#website to extract header entries from. 
#can add more websites, or different websites.
#behavior of scraper may be different, however
webpage = 'https://www.        .com' 

request = requests.get(webpage)
soup = BeautifulSoup(request.text, 'html.parser')
#making string nice looking
prettyString = soup.prettify().encode('utf-8').strip()

##########################################################

#array to hold the website entries from website
titles_HTML = []

#putting all elements on webpage that have the class entry-title
#into this array
titles_HTML = soup.find_all(attrs={'class':'entry-title'})

#stripping the entries in titles_HTML to get nice entries
titles = []
for i in titles_HTML:
	  titles.append(i.text.strip())

#printing titles nicely to stdout
for i in range(0,5):
   print('#' + str(i+1) + ' ' + str(titles[i]))
