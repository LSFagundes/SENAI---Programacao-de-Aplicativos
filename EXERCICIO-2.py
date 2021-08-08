i=0
lista=[] 
soma=0
quantidade = int(input("Quantos itens você deseja inserir na lista? "))
while i <= quantidade-1:
   item = int(input("Digite os itens: "))
   lista.append(item)
   if quantidade == 1:
      break
   i+=1 

for i in lista:
    soma+=i
soma / quantidade
print(soma)
if soma > 1:
    print ("O número é positivo")
else:
    print ("O número é negativo")
