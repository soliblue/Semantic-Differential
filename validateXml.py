from lxml import etree
from io import StringIO
import sys

newspaper = "Almasryalyoum"
file = "data/" + newspaper +"_utf_8.xml"

with open(file,"r",encoding="utf-8") as xml_file:
	xml_to_check = xml_file.read()
	print(xml_to_check[0:100])
	# parse xml
	try:
	    doc = etree.parse(StringIO(xml_to_check))
	    print('XML well formed, syntax ok.')

	# check for file IO error
	except IOError:
	    print('Invalid File')

	# check for XML syntax errors
	except etree.XMLSyntaxError as err:
	    print('XML Syntax Error, see error_syntax.log')
	    with open('error_syntax.log', 'w') as error_log_file:
	        error_log_file.write(str(err.error_log))
	    quit()

	except:
	    print('Unknown error, exiting.')
	    quit()
