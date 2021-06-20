l = []
def numeracao():
    for chave, valor in enumerate(l, start=1):
        print (chave,")", valor)
    
i=0 
quantidade = int(input("Quantos itens você deseja inserir na lista? "))
while i <= quantidade-1:
   item = str(input("Digite os itens desejados: "))
   l.append(item)
   if quantidade == 1:
      break
   i+=1 


numeracao()


    