produtos = [
    {"nome": "Teclado", "preco": 120.0},
    {"nome": "Mouse", "preco": 45.0},
    {"nome": "Monitor", "preco": 750.0}
]
for produto in produtos:
    if produto["preco"] > 50:
        print(produto["nome"])
