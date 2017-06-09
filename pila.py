from NodoPila import NodoPila

class Pila():
	def __init__(self):
		self.cabeza=None
		self.siguiente=None
	def push(self,valor):
		pila=Pila()	
		pila.valor=valor
		if self.cabeza==None:
			self.cabeza=pila
		else:
			pila.siguiente=self.cabeza
			self.cabeza=pila
	def pop(self):
		if self.cabeza!=None:
			tmp=self.cabeza
			self.cabeza=self.cabeza.siguiente
			return tmp
		else:
			return None

