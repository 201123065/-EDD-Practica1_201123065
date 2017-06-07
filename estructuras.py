#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from usuario import usuario
from listado_menu import main_menu,addUser	

print "Practica 1 EDD"
valor= True
os.system("clear")
while valor:
	menu = main_menu()
	print "ingrese dato>>"
	valor=raw_input()
	os.system("clear")
	if str(valor)=="1":
		menu=addUser()
		username=raw_input()
		print "contraseña"
		passwd=raw_input()
	elif str(valor)=="2":
		pri
	elif str(valor)=="3":
		print "Gracias por utilizar el programa"
		valor=False
		break
	
	os.system("clear")

