#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from usuario import usuario
from listado_menu import *
from parseXML import parser
from pila import Pila

usuario = usuario()
sesion_usuario=None

def menu_matriz(usuario):
	xance="1"
	while xance!="5":
		menu=menu3()
		xance=raw_input()
		if xance=="1":
			menu=menu3_opcion1()
			for x in range(0,usuario.mat.retornarX()):
				for y in range(0,usuario.mat.retornarY()):
					print "ingrese el dato para la casilla["+str(x+1)+","+str(y+1)+"]"
					val=raw_input()
					usuario.mat.cargar(x,y,val)
		elif xance=="2":
			for x in range(0,usuario.mat.retornarY()):
				for y in range(0,usuario.mat.retornarX()):
					celda= usuario.mat.ret_valor(x,y)
					usuario.trans.cargar(x,y,celda)


			print "transpuesta generada correctamente "

		elif xance=="3":
			usuario.mat.mostrarMat()
		elif xance=="4":
			usuario.trans.mostrarMat()
		elif xance=="5":
			print "regreso"
		else:
			print " esta no es una opcion valida"




def postorden(cadena):
	save=""
	if cadena is not None:
		pila=Pila()
		print "la operacion a efectuar es: "+cadena.operacion
		for c in cadena.operacion:
			if c =="*": 
				A=int(pila.pop().valor)
				B=int(pila.pop().valor)
				C=A*B
				print " se multiplico "+str(B)+" por "+str(A)
				pila.push(str(C))
			elif c =="+":
				A=int(pila.pop().valor)
				B=int(pila.pop().valor)
				C=A+B
				print " se sumo "+str(B)+" mas "+str(A)
				pila.push(str(C))
			elif c =="-":
				A=int(pila.pop().valor)
				B=int(pila.pop().valor)
				C=B-A
				print " se resto "+str(B)+" menos "+str(A)
				pila.push(str(C))
			elif c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9" :
				save=save+c
				print " se cargo "+c+" a la pila "
			else:
				if save!="":
					pila.push(save)
					save=""
		print "resultado="+pila.pop().valor

	else:
		print "la cola parece estar vacia"


print "Practica 1 EDD"
valor= True
os.system("clear")
menu=Bienvenido()
while valor:
	menu = main_menu()
	print "ingrese dato>>"
	valor=raw_input()
	os.system("clear")
	if str(valor)=="1":
		menu=menu1_opcion1()
		username=raw_input()
		print "contraseña"
		passwd=raw_input()
		os.system("clear")
		print usuario.agregar(username,passwd)
	elif str(valor)=="2":
		menu=menu1_opcion2()
		username = raw_input()
		print "ingrese la contraseña:"
		passwd = raw_input()
		menu_2=True
		os.system("clear")
		sesion_usuario=usuario.existe(username,passwd)
		if sesion_usuario!=None:
			os.system("clear")
			while menu_2==True:
				menu=menu2(str(sesion_usuario.usuario))
				opcion = raw_input()
				os.system("clear")
				if opcion=="1":
					menu=menu2_opcion1()
					ruta = raw_input()
					sesion_usuario=parser(ruta,sesion_usuario)
				elif opcion=="2":
					if sesion_usuario.mat==None:
						print "por favor cargue primero el archivo xml"
					else:
						xance="1"
						while xance!="2":
							menu=menu2_opcion2()
							xance=raw_input()
							os.system("clear")
							if xance=="1":
								linea()
								postorden(sesion_usuario.cola.dequeque())
								linea()

				elif opcion=="3":
					if sesion_usuario.mat==None:
						print "por favor cargue primero el archivo xml"
					else:
						os.system("clear")
						menu=menu_matriz(sesion_usuario)
				elif opcion=="4":
					menu=lista_users()
					usuario.imprime_usuarios()
					print"cuatro"
				elif opcion=="5":
					sesion_usuario.cola.pcola()
				elif opcion=="6":
					menu_2=False
					menu=close_session()
				else:
					menu=mistake()


		else:
			menu=mistake()
	elif str(valor)=="3":
		menu = gracias()
		valor=False
		break
	else:
		menu=mistake()





