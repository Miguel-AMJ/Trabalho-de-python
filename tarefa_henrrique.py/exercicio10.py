boletim = {}
while True:
    opcao = input("Deseja adicionar um aluno? (s/n): ")
    if opcao == "n" or opcao == "N":
        break
    if opcao == "s" or opcao == "S":
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        boletim[nome] = nota
    else:
        print("Digite s para sim ou n para não.")

for aluno, nota in boletim.items():
    if nota >= 6.0:
        print(aluno, ": Aprovado")
    else:
        print(aluno, ": Reprovado")
