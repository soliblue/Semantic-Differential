import requests
from bs4 import BeautifulSoup
import re

def save_file(content,fileName):
	file = open('masryElYom/' + fileName + '.txt', 'w')
	file.write(content)
	file.close()

url = 'https://www.almasryalyoum.com/'
articles_url = url + 'news/details/'

# Articles 1 to 2000 already crawled
for article_id in range(1000,2000):
	article = requests.get(articles_url + str(article_id))
	print(articles_url + str(article_id))
	soup = BeautifulSoup(article.content, 'html.parser')
	paragraphs = soup.find(id='NewsStory').findAll('p')
	paragraphs = "\n".join([paragraph.getText() for paragraph in paragraphs])
	save_file(paragraphs.encode('utf-8'),'article' + str(article_id))