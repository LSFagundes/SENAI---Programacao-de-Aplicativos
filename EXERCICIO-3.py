from typing import Any
lista = []
print ("Tigite 20 números: ")
while len(lista) < 20:
    item = (int(input()))  
    lista.append(item)
print("A média dos números digitados é: ", sum(lista)/len(lista))
x = max(lista)
print("O maior valor é:", x)
x = min(lista) 
print("O menor valor é:", x)