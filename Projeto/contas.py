# -*- coding: iso8859-1 -*-

from collections import namedtuple

import menu


contaReg = namedtuple("contaReg", "id, tipo, descricao, banco, dataabertura, saldo")
listaContas = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaContas)):
        if listaContas[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_contas_movimentos():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    tipo = raw_input("Qual o tipo do titular? ")
    descricao = raw_input("Qual das opcoes?")
    banco = raw_input("Qual a instituicao bancaria?")
    dataabertura = raw_input("Qual o dia de Abertura na instituicao?")
    saldo = raw_input("Qual o saldo a depositar?")
    
    
    
    contas = contaReg(cod, tipo, descricao, banco, dataabertura, saldo)
    listaContas.append(contas)


def pesquisar_contas():
    cod = input("Qual o codigo da conta? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Nao existe conta com esse código"
        return

    print "Codigo: ", listaContas[pos].id
    print "Tipo: ", listaContas[pos].tipo
    print "Descricao: ", listaContas[pos].descricao
    print "Banco: ", listaContas[pos].banco
    print "DataAbertura: ", listaContas[pos].dataabertura
    print "Saldo: ", listaContas[pos].saldo
    
def efetuar_transferencia():
           
    print "Numero de contas:", len(listaContas)               

    numeroOrigem = input("Qual o numero da conta de origem?")
    encontrou = False
    
    global posOrigem    
    global posDestino
    
   
    
   
    posOrigem = encontrar_posicao(numeroOrigem)

    if posOrigem == -1:
        print "Nao existe conta com esse código"
        return
       
    
    numeroDestino = input("Qual o numero da conta de destino?")
    encontrou = False
    posDestino = None
    for i in range(len(listaContas)):
        if listaContas[i].id == numeroDestino:
            encontrou = True
            
            posDestino = i
            break
    
    if not encontrou:
        print "Conta não existe"
        return        
        
    
    montante = input("Qual o montante a transferir?")
    
    saldoOrigem = listaContas[posOrigem].saldo
    listaContas[posOrigem] = listaContas[posOrigem]._replace(saldo=saldoOrigem-montante)
    
    saldoDestino = listaContas[posDestino].saldo
    listaContas[posDestino] = listaContas[posDestino]._replace(saldo=saldoDestino+montante)
    
    print "Transferência efetuada"
    

                
    


def listar_contas():
    for i in range (len(listaContas)):
        print "Código: ", listaContas[i].id
        print "Tipo: ", listaContas[i].tipo
        print "Descricao: ", listaContas[i].descricao
        print "Banco: ", listaContas[i].banco
        print "DataAbertura: ", listaContas[i].dataabertura
        print "Saldo: ", listaContas[i].saldo
  

def eliminar_contas():
    cod = input ("Código do conta a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe aluno com esse código"
        return

    # TODO: Confirmar eliminação
    listaContas.pop(pos)


    
def alterar_contas():
    cod = input ("Código do conta a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe conta com esse código"
        return

    # só altera o nome
    novotipo = raw_input("Qual o novo tipo de titular? ")
    novadescricao = raw_input("Qual a nova descrição?")
    novobanco = raw_input("Qual o banco?")
    novadataabertura = raw_input("Qual a data de abertura?")
    novosaldo = raw_input("Qual o saldo que deseja depositar?")
    
    listaContas[pos] = listaContas[pos]._replace(tipo=novotipo, descricao=novadescricao, banco=novobanco, dataabertura=novadataabertura, saldo=novosaldo)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.contas()

        if op == '1':
            inserir_contas_movimentos()
        elif op =='2':
            listar_contas()
        elif op == '3':
            pesquisar_contas()
        elif op == '4':
            alterar_contas()
        elif op == '5':
            eliminar_contas()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"










