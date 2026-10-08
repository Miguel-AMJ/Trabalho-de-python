numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

contador = 10
while contador >= 1:
    print(contador)
    contador = contador - 1
print("Fogo!")

numero = int(input("Digite um número de 1 a 10: "))
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

numeros = [3, 8, 15, 22, 27, 34, 41, 50]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares = pares + [numero]
print(pares)

contato = {}
nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
email = input("Digite seu e-mail: ")
contato["nome"] = nome
contato["telefone"] = telefone
contato["email"] = email
print(contato)

notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}
soma = 0
quantidade = 0
for nota in notas.values():
    soma = soma + nota
    quantidade = quantidade + 1
media = soma / quantidade
print(media)

senha_secreta = "python123"
senha = ""
while senha != senha_secreta:
    senha = input("Digite a senha: ")
print("Acesso Liberado")

produtos = [
    {"nome": "Teclado", "preco": 120.0},
    {"nome": "Mouse", "preco": 45.0},
    {"nome": "Monitor", "preco": 750.0}
]
for produto in produtos:
    if produto["preco"] > 50:
        print(produto["nome"])

palavra = input("Digite uma palavra: ")
vogais = []
for letra in palavra:
    if letra in "aeiouAEIOU":
        vogais = vogais + [letra]
print(vogais)

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
