vetorNome = []

for i in range(5):
    nome = input("Digite o nome: ")
    vetorNome = vetorNome + [nome]
for y in range (5):
    print(vetorNome[y])
print()
for x in range(4,-1,-1):
   print(vetorNome[x])