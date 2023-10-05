n = int(input("n: "))
vetorA = [0] *n
vetorB = [0] *n
vetorS = [0] *n

for i in range (n):
    vetorA[i] =int(input("a:"))
    vetorB[i] =int(input("b:"))
    vetorS[i] = vetorA[i] + vetorB[i]

print(vetorA)
print('+   '*n)
print(vetorB)
print('=   '*n)
print(vetorS)