palavra = input("Digite uma palavra: ")
vogais = []
for letra in palavra:
    if letra in "aeiouAEIOU":
        vogais = vogais + [letra]
print(vogais)
