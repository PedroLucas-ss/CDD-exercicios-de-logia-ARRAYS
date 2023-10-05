vetorNums = []
vetorPares = []
vetorMaiorMenor = []
somaNums = 0
maiorMedia = 0

for i in range(3):
    num = int(input("Digite um numero: "))
    vetorNums = vetorNums + [num]
    somaNums += num
numMaior = vetorNums[0]
numMenor = vetorNums[0]
for x in range(3):
    if vetorNums[x] % 2 == 0:
        vetorPares = vetorPares + [vetorNums[x]]

for y in range(3):

    if vetorNums[y] >= numMaior:
        numMaior = vetorNums[y]

    if vetorNums[y] <= numMenor:
        numMenor = vetorNums[y]

vetorMaiorMenor = vetorMaiorMenor + [numMenor] + [numMaior]

media = somaNums /3

for z in range(3):
    if vetorNums[z] > media:
        maiorMedia += 1

print(vetorNums)
print(vetorPares)
print(vetorMaiorMenor)
print(maiorMedia)
