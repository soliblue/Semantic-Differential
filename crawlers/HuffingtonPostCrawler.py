from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def save_file(content,fileName):
	file = open('solution_bonus/' + fileName + '.txt', 'w')
	file.write(content)
	file.close()

req = Request('https://www.huffingtonpost.de/politik/', headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
page = urlopen(req).read()


soup = BeautifulSoup(page, 'html.parser')
links = soup.findAll('a',class_="yr-card-headline")

headlines = ""

for link in links:
	headlines += link.getText()
	print(link.getText())
    
save_file(headlines,"headlines")