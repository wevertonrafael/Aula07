nomes =["joão", "carlos", "maria", "luiza", "isabel"]
aluno = (input("Digite um nome: "))
mensagem = "não estar na lista"
for x in range (len(nomes)):
    if aluno ==nomes[x]:
        mensagem = f"Aluno encontrado: {nomes[x]}, {x} "
        break
print(mensagem)
