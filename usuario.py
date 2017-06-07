from NodoUsuario import NodoUsuario

class usuario():
	def __init__(self):
		self.inicio=None
		self.puntero=None
	def agregar(self,usuario,passwd):
		nuevoUser = NodoUsuario(usuario,passwd,None,None)
		if self.puntero==None:
			nuevoUser.derecha=nuevoUser
			nuevoUser.izquierda=nuevoUser
			self.puntero=nuevoUser
			self.inicio=nuevoUser
			self.tam=1
			return True
		else:
			tmp = self.inicio
			if tmp.usuario==usuario:
				return False
			while tmp.derecha!=self.inicio:
				tmp=tmp.derecha
				if tmp.usuario==usuario:
					return False
			nuevoUser.derecha=self.inicio
			self.inicio.izquierda=nuevoUser
			nuevoUser.izquierda=self.puntero
			self.puntero.derecha=nuevoUser
			self.puntero=nuevoUser
			return True

	def existe(self,usuario,passwd):
		if self.puntero==None:
			return False
		else:
			tmp = self.inicio
			if tmp.usuario==usuario and tmp.passwd==passwd:
				return True
			while tmp.derecha!=self.inicio:
				tmp=tmp.derecha
				if tmp.usuario==usuario and tmp.passwd==passwd:
					return True
		return False


