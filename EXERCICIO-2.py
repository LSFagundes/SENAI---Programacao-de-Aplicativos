i=0
lista=[] 
soma=0
print ("Digite 4 números: ")
while len(lista) < 4:
    item = (int(input()))  
    lista.append(item)
for i in lista:
    soma+=i
soma / 4
print("A soma dos Números é:", soma)
if soma > 1:
    print ("O número é positivo")
else:
    print ("O número é negativo")
