# -*- coding: iso8859-1 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gest�o de Contas"
    print "   2. "
    print 
    print "   0. Sair"
    print 

    op = raw_input("Op��o: ")
    return op


def contas():
    print
    print " *** Menu Contas **** "
    print
    print "1. Inserir nova conta"
    print "2. Listar todas contas"
    print "3. Pesquisar conta"
    print "4. Alterar movimentos de uma conta"
    print "5. Eliminar conta"
    print 
    print "0. Menu Anterior"

    op = raw_input("Op��o: ")
    return op



if __name__ == "__main__":
    print "Este programa n�o deve ser executado diretamente"

