from bs4 import BeautifulSoup
newspaper = "Almasryalyoum"
filePath = "data/" + newspaper +"_utf_8.xml"
file = open(filePath,"r")
contents = file.read()
soup = BeautifulSoup(contents,'xml')
titles = soup.find_all('Almasryalyoum')
print(titles[0])
print(titles[len(titles) - 1])
print(len(titles))