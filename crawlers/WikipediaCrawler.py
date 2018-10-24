import requests
from bs4 import BeautifulSoup
import re

def save_file(content,fileName):
	file = open('solution_one/' + fileName + '.txt', 'w')
	file.write(content)
	file.close()

page = requests.get('https://en.wikipedia.org/wiki/Web_design')
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')


# Retrieve all of the links
pageLinks = soup.findAll("a",href=True)

savedPages = []

# Iterate over collected links
# Load the page and save intro in seperate document
for pageLink in pageLinks:
    try:
        page = requests.get('https://en.wikipedia.org' + pageLink['href'])
        contents = page.content
        soup = BeautifulSoup(contents, 'html.parser')
    
        introDiv = soup.find('div',class_="mw-parser-output")
        if introDiv:
            children = introDiv.findChildren('p')
            if len(children) > 0:
                intro = children[0].text
            title = soup.find('h1',class_="firstHeading").text
            title = re.sub('\W+','', title)
            if title not in savedPages:
                save_file(intro,title)
                savedPages.append(title)
    except requests.exceptions.RequestException as e:
        print("Broken link")