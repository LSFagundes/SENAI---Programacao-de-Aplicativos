from typing import Any
lista = [5,7,2,9,4,1,3]

print("Tamanho da lista")
print(len(lista))

print("Maior valor do lista")
x = max(lista)
print(x) 
print("menor valor da lista")
x = min(lista)
print(x) 
print("soma de todos os elementos da lista")
x= sum(lista)
print (x)  
print("lista em ordem crescente")
lista.sort()
print(lista)
print("lista em ordem decrescente")
lista.sort(reverse=True)
print(lista)