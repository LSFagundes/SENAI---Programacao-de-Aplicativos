from typing import Any
lista = [5,7,2,9,4,1,3]
maior = 0
menor = 0 

for i in range(len(lista)):
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i]> maior:
            maior = lista[i]
        if lista[i] < menor:
           menor = lista[i]
   
def decrescente():
    for numero in range(len(lista)-1,0,-1):
        for i in range(numero):
            if lista[i]<lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
def crescente():
    for numero in range(len(lista)-1,0,-1):
        for i in range(numero):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
def adicao():
    soma=0
    for i in lista:
        soma+=i
    print(soma)
print("Tamanho da lista")
print(len(lista))
print("Maior valor da lista")
print(maior)
print("menor valor da lista")
print(menor)
print("soma de todos os elementos da lista")
adicao
print("lista em ordem crescente")
crescente
print(lista)
print("lista em ordem decrescente")
decrescente
print(lista)