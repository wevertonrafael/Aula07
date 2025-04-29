A=[5,6,7,8,9]
numero = int(input("Digite um número: "))
multiplicacao=[""]*5
for x in range (len(A)):
    multiplicacao[x]=numero*A[x]
print(multiplicacao)
