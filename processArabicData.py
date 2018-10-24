from xml.dom import minidom
from xml.parsers.expat import ExpatError

# newspaper name
newspaper = "Almasryalyoum"
filePath = "data/" + newspaper +"_utf_8.xml"


xml_file = open(filePath,"r+",encoding="utf-8")
lines = xml_file.readlines()


# parse the xml file corresponding to the newspaper
# catch errors in the file and fix them
has_erros = True
lastError = {"position":(0,0),"count":0}
errorSymbols = ["<","&"]
while(has_erros):
	try:
		mydoc = minidom.parseString("".join(lines))
		has_erros = false
	except ExpatError as e:
		e = str(e)
		print("Error Message: " + e)
		line = int(e[e.find("line") + 5:e.find(",")])
		column = int(e[e.find("column") + 7:])
		if (line,column) == lastError["position"]:
			lastError["count"] += 1
		else:
			lastError["position"] = (line,column)
			lastError["count"] = 0
		print("Corresponding line: " + lines[line - 1])
		if lines[line - 1][column - 1] in errorSymbols:
			lines[line - 1] = lines[line - 1][0:column - 1] + lines[line - 1][column:]
		if lastError["count"] > 2:
			lines[line - 1] = lines[line - 1].replace("&","")
		if lastError["count"] > 3:
			lines[line - 1] = lines[line - 1].replace("<","")

new_xml_file = open("data/" + newspaper + "_fixed" +"_utf_8.xml","w+")
new_xml_file.write("".join(lines))
new_xml_file.close()

# get the articles from the xml file
articles = mydoc.getElementsByTagName(newspaper + "Data")

for article in articles:
	print(article)
	break