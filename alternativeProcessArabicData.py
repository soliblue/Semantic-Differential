from xml.dom import minidom
from xml.parsers.expat import ExpatError

# the chars which cause trouble are < and & when they come in
# the text of the articles
# we could read the file as a string and iterate
# over all chars and check whether it is a < or &
# we need to make sure not to replace < for the normal xml tags

# newspaper name
newspaper = "Almasryalyoum"
filePath = "data/" + newspaper +"_utf_8.xml"


# xml_file = open(filePath,"r+",encoding="utf-8")
# content = xml_file.read()
# new_content = ""
# charIndex = 0
# length = len(content) - 1
# for char in content:
# 	if char == "&":
# 		new_content += '&amp;'
# 		print("Chars left: " + str(length - charIndex))
# 	elif char == "<" and content[charIndex + 1] not in ["T","I","U","A","H","/","?","D"]:
# 		new_content += '&lt;'
# 		print("Chars left: " + str(length - charIndex))
# 	else:
# 		new_content += char
# 	if charIndex < length - 1:
# 		charIndex += 1

new_xml_file = open("data/" + newspaper + "_fixed2" +"_utf_8.xml","r+")
# new_xml_file.write(new_content)
lines = new_xml_file.readlines()
mydoc = minidom.parseString("".join(lines))
# get the articles from the xml file
articles = mydoc.getElementsByTagName(newspaper + "Data")

for article in articles:
	print(article.getElementsByTagName("Text")[0].firstChild.data)
	break
