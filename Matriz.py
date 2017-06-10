from nodoMatriz import NodoMatriz

class Matriz():
	def __init__(self):
		self.raiz=None
		self.x=0
		self.y=0
	def crear(self,x,y):
		self.x=int(x)
		self.y=int(y)
		rolX=0
		rolY=0
		superior=None
		tmp=None
		preview=None
		while rolY<int(y):
			while rolX<int(x):
				if rolY==0: 
					if rolX==0:
						self.raiz=NodoMatriz()
						superior=self.raiz
						tmp=self.raiz
						self.raiz.valor=0
					else:
						temp = NodoMatriz()
						temp.valor=0
						temp.izquierda=tmp
						tmp.derecha=temp
						tmp=temp
				else:
					temp=NodoMatriz()
					temp.valor=0
					if rolX==0:
						tmp=superior
						superior=temp
						preview=temp
					else:
						temp.izquierda=preview
						preview.derecha=temp
						preview=temp

					temp.arriba=tmp
					tmp.abajo=temp
					tmp=tmp.derecha
				rolX=rolX+1
			rolX=0
			rolY=rolY+1
	def cargar(self,ejeX,ejeY,valor):
		temp=self.raiz
		if self.x>=ejeX and self.y>=ejeY:
			if ejeX>=0 and self.y>=0:
				pos=0
				while pos<ejeX:
					temp=temp.derecha
					pos=pos+1
				pos=0
				while pos<ejeY:
					temp=temp.abajo
					pos=pos+1
				temp.valor=valor
			else:
				print "el valor no puede ser menor o igual a cero(0)"
		else:
			print "esta posicion no existe en esta matriz"

	def mostrarMat(self):
		cad=""
		if self.raiz!=None:
			temporal=self.raiz
			follow = self.raiz
			while temporal!=None:
				while follow!=None:
					cad=cad+str(follow.valor)+"  "
					follow=follow.derecha
				cad=cad+"\n"
				temporal=temporal.abajo
				follow=temporal
		print cad

	def transpuesta(self):
		cad=""
		if self.raiz!=None:
			temporal=self.raiz
			follow = self.raiz
			while temporal!=None:
				while follow!=None:
					cad=cad+str(follow.valor)+"  "
					follow=follow.abajo
				cad=cad+"\n"
				temporal=temporal.derecha
				follow=temporal
		print cad

	def ret_valor(self,y,x):
		tmp = self.raiz
		for x in range(0,x):
			tmp=tmp.derecha
		for y in range(0,y):
			tmp=tmp.abajo
		return tmp.valor


	def retornarX(self):
		return self.x
	def retornarY(self):
		return self.y