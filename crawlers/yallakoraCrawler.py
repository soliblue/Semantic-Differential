import requests
from bs4 import BeautifulSoup
import re

def save_file(content,fileName):
	file = open('yallakora/' + fileName + '.txt', 'w')
	file.write(content)
	file.close()

url = 'http://www.yallakora.com/'
articles_url = url + 'News/'

# Articles 1 to 1000 already crawled
# http://www.yallakora.com/News/119900
#  start at 1199
# add 1 every iteration
# done: 1199 to 2199
for article_id in range(1199,2199):
	article = requests.get(articles_url + str(article_id) + '00',headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
	print(article)
	print(articles_url + str(article_id) + '00')
	soup = BeautifulSoup(article.content, 'html.parser')
	try:
		paragraphs = soup.find('article').findAll('p')
		paragraphs = "\n".join([paragraph.getText() for paragraph in paragraphs])
		save_file(paragraphs.encode('utf-8'),'article' + str(article_id))
	except:
		print("error")