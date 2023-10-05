vetor = [0]*30

print(vetor)
for i in range(30):
    vetor[i] = int(input("Digite um numero: "))
num = int(input("Digite o numero que deseja buscar: "))
somaNum=0
for x in range(30):
    if vetor[x] == num:
        somaNum += 1
print(somaNum)