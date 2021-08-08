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
def tamanhoLista(lista): 
    conta=0
    for i in lista:
        conta += 1
    return conta
def decrescente(lista):
    if tamanhoLista(lista) <= 1:
        sLista = lista 
    else:
        for numero in range(tamanhoLista(lista)-1,0,-1):
            for i in range(numero):
                if lista[i]<lista[i+1]:
                    temp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = temp
        sLista = lista
    return sLista
def crescente(lista):
    if tamanhoLista(lista) <= 1:
        sLista = lista 
    else:
        for numero in range(tamanhoLista(lista)-1,0,-1):
            for i in range(numero):
                if lista[i]>lista[i+1]:
                    temp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = temp
        sLista = lista
    return sLista
def adicao():
    soma=0
    for i in lista:
        soma+=i
    print (soma)

print("Tamanho da lista")
print (tamanhoLista(lista))
print("Maior valor da lista")
print(maior)
print("Menor valor da lista")
print(menor)
print("Soma de todos os elementos da lista")
adicao()
print("Lista em ordem crescente")
crescente(lista)
print(lista)
print("lista em ordem decrescente")
decrescente(lista)
print(lista)