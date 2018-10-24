import requests
from bs4 import BeautifulSoup
import re

def save_file(content,fileName):
	file = open('akhbarElYom/' + fileName + '.txt', 'w')
	file.write(content)
	file.close()

url = 'https://akhbarelyom.com/'
articles_url = url + 'news/newdetails/'

# Articles 1 to 2000 already crawled
for article_id in range(467,2000):
	try:
		article = requests.get(articles_url + str(article_id))
		print(articles_url + str(article_id))
		soup = BeautifulSoup(article.content, 'html.parser')
		paragraphs = soup.find('section',{'class':'articleBody'}).findAll('p')
		paragraphs = "\n".join([paragraph.getText() for paragraph in paragraphs])
		save_file(paragraphs.encode('utf-8'),'article' + str(article_id))
	except: 
		print("error")