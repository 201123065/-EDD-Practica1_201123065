#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from usuario import usuario
from listado_menu import *
from parseXML import parser

usuario = usuario()
sesion_usuario=None

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
						print "exitoo"
					print"dos"
				elif opcion=="3":
					if sesion_usuario.mat==None:
						print "por favor cargue primero el archivo xml"
					else:
						print "exitoo"
				elif opcion=="4":
					usuario.imprime_usuarios()
					print"cuatro"
				elif opcion=="5":
					print"cinco"
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

