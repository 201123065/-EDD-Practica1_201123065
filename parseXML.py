import xml.etree.ElementTree as parse

def parser(cadena,user):
	try:
		root = parse.parse(cadena)
		doc = root.getroot()
		print doc.tag
		print root.find('matriz/x').text
		print root.find('matriz/y').text 
	except IOError:
		print "este archivo no existe en esta carpeta"