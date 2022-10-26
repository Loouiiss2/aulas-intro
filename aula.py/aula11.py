clubes =[]
for i in range(10):

    clubes = input("digite o novo clube: ")
    clubes.append(clube)

clube_pesquisar = input("digite o novo clube: ")
#forma 1
for c in clubes:

    if clube_pesquisa.upper() == astr(c).upper():
        print("achei")

        #forma 2
        if clube_pesquisa in clubes:
            print("achei")
    else:
        print("não achei!")

        

    

from ctypes import HRESULT
from traceback import print_list


notas = []
#criação de notas
for i in range(20):
    notas.append(float(input("digite uma nota:" )))

#soma
for nota: in notas:
   acumuladora = acumuladora + nota

   # media

   media =acumuladora / len (notas)

for n in notas:
    if n > media:
        contador += 1
        #contador


#Questão 4
from random import randint

lista_num = []
nova_lista = []

for i in range(10):
    lista_num.append(randint(0,100))
    
    x =randint(0,9)

x = range(len(lista_num)):
    nova_lista.append(x * lista_num[i])

    print(lista_num)
    print(x)
    print(nova_lista)