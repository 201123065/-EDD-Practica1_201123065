from NodoUsuario import NodoUsuario

class usuario():
	def __init__(self):
		self.inicio=None
		self.puntero=None
	def agregar(self,usuario,passwd):
		nuevoUser = NodoUsuario(usuario,passwd,None,None)
		verdad="***************************************\n** usuario creado satisfactoriamente **\n***************************************"
		mentira="***************************************\n******** este usuario ya existe ********\n***************************************"
		if self.puntero==None:
			nuevoUser.derecha=nuevoUser
			nuevoUser.izquierda=nuevoUser
			self.puntero=nuevoUser
			self.inicio=nuevoUser
			self.tam=1
			return verdad
		else:
			tmp = self.inicio
			if tmp.usuario==usuario:
				return mentira
			while tmp.derecha!=self.inicio:
				tmp=tmp.derecha
				if tmp.usuario==usuario:
					return mentira
			nuevoUser.derecha=self.inicio
			self.inicio.izquierda=nuevoUser
			nuevoUser.izquierda=self.puntero
			self.puntero.derecha=nuevoUser
			self.puntero=nuevoUser
			return verdad

	def existe(self,usuario,passwd):
		if self.inicio==None:
			return None
		else:
			tmp = self.inicio
			if tmp.usuario==usuario and tmp.passwd==passwd:
				return tmp
			while tmp.derecha!=self.inicio:
				tmp=tmp.derecha
				if tmp.usuario==usuario and tmp.passwd==passwd:
					return tmp
		return None

	def imprime_usuarios(self):
		temporal = self.inicio
		izq_a_der=temporal.usuario
		while temporal.derecha!=self.inicio:
			temporal=temporal.derecha
			izq_a_der=izq_a_der+"->"+temporal.usuario
		izq_a_der=izq_a_der+"->"+temporal.derecha.usuario
		
		temporal=self.inicio.izquierda
		der_a_izq =temporal.usuario
		while temporal.izquierda!=self.inicio.izquierda:
			temporal=temporal.izquierda
			der_a_izq=der_a_izq+"->"+temporal.usuario
		der_a_izq=der_a_izq+"->"+temporal.izquierda.usuario
		print izq_a_der +"\n"+der_a_izq






