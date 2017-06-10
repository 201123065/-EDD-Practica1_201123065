# import xml.etree.ElementTree as parse
import os
from xml.etree import ElementTree
from Matriz import Matriz
from cola import Cola
def parser(cadena,user):
	try:
		full_file =os.path.abspath(os.path.join(cadena))
		dom = ElementTree.parse(full_file)
		if user.mat==None:
			ejex=dom.find('matriz/x').text
			ejey=dom.find('matriz/y').text
			matriz= Matriz()
			matriz.crear(ejey,ejex)
			user.mat=matriz
			trans = Matriz()
			trans.crear(ejex,ejey)
			user.trans=trans

		cola = Cola()
		operacion = dom.findall('operaciones/operacion')
		if user.cola ==None:
			for op in operacion:
				cola.queque(op.text)
			user.cola=cola
		else:
			for op in operacion:
				user.cola.queque(op.text)
		print "----------cargado exitosamente----------"

	except IOError:
		print "este archivo no existe en esta carpeta"
	
	return user