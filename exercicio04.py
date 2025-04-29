notas = [""]*5
soma = 0
contador=0
for x in range(5):
    notas[x]=float(input("digite a nota: "))
for j in range(5):
    soma=soma+notas[j]
    media=soma/5

for i in range(5):
    if notas[i]>media:
        contador=contador+1

print(f"{contador} notas são maiores que a media {media}")



