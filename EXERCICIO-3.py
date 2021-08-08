from typing import Any
lista = []
maior=0
menor=0
soma=0
  
print ("Tigite 20 números: ")
while len(lista) < 20:
    item = (int(input()))  
    lista.append(item)
for i in lista:
        soma += i 
print("A média dos números digitados é: ", soma /20) 

for i in range(len(lista)):
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i]> maior:
            maior = lista[i]
        if lista[i] < menor:
           menor = lista[i]
print("O maior valor é:", maior)
print("O menor valor é:", menor)