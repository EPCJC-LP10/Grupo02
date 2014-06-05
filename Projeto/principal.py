# -*- coding: iso8859-1 -*-

import menu
import contas
import util


# nome dos ficheiros
fxContas = "fxContas.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	contas.listaContas = util.ler_ficheiro(fxContas)
     

def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxContas, contas.listaContas)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        contas.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()


