import requests
from bs4 import BeautifulSoup
import re

def save_file(content,fileName):
	file = open('solution_one/' + fileName + '.txt', 'w')
	file.write(content)
	file.close()

page = requests.get('https://www.almasryalyoum.com/')
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')


# Retrieve all of the links
pageLinks = soup.findAll("a",href=True)

savedPages = []

# Iterate over collected links
# Load the page and save intro in seperate document
for pageLink in pageLinks:
    try:
    	link = pageLink.get('href')
    	if '/news/details/' in link:
    		print(link)
    except requests.exceptions.RequestException as e:
        print("Broken link")