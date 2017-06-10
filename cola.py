from nodoCola import nodoCola

class Cola():
	def __init__(self):
		self.cabeza=None
		self.cola=None
	def queque(self,operacion):
		if self.cabeza==None:
			self.cabeza=nodoCola(operacion,None)
			self.cola=self.cabeza
		else:
			self.cola.siguiente = nodoCola(operacion,None)
			self.cola=self.cola.siguiente

	def dequeque(self):
		if self.cabeza!=None:
			retorno = self.cabeza
			self.cabeza=self.cabeza.siguiente
			return retorno
		else:
			return None
	def pcola(self):
		punta=self.cabeza
		val=0
		if punta!=None:
			while punta!=None:
				print "operacion"+str(val)+":"+punta.operacion
				punta=punta.siguiente
				val=val+1
		else:
			print "la cola parece estar vacia"

		
