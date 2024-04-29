import json

produto1: str = "sapato"
produto2: str = "cavalo"
produto3: str = "caixa"


produtos: list = []
produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)
print(produtos)

produtos_dict1: dict = {
    "nome": "sapato",
    "preco": 100.00,
    "quantidade": 10,
    "disponibilidade": True
}

produtos_dict2: dict = {
    "nome": "caixa",
    "preco": 25.00,
    "quantidade": 15,
    "disponibilidade": True
}

carrinho_dict: list = []

carrinho_dict.append(produtos_dict1)
carrinho_dict.append(produtos_dict2)

print(carrinho_dict)
carrinho_json = json.dumps(carrinho_dict)

lista_elementos: list = produtos_dict2.items()
print(lista_elementos)

carrinho_dict_dict: dict = {
    "produto1":{
    "nome": "sapato",
    "preco": 100.00,
    "quantidade": 10,
    "disponibilidade": True},

    "produto2":{
    "nome": "caixa",
    "preco": 25.00,
    "quantidade": 15,
    "disponibilidade": True}
}

carrinho_items = carrinho_dict_dict.items()
print(type(carrinho_items))
print(carrinho_items)


print("///")

for i, j in carrinho_dict_dict['produto1'].items():
    print(i)
    print(j)