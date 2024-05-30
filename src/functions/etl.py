import csv


def ler_csv(arquivo: str) -> list[dict]: 
    """
    Função que lê um arquivo csv e retorna uma lista de dicionários.
    """
    lista_csv: list[dict] = []

    with open(file=arquivo, mode="r", encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            lista_csv.append(row)

    return lista_csv

csv_arquivo = "tests/functions/vendas.csv"

def filtrar_produtos_entregues(lista_csv: list[dict]) -> list[dict]:
    """
    Função que recebe uma lista de dicionários e retorna uma lista de dicionários com os produtos entregues.
    """
    lista_produtos_entregues: list[dict] = []
    for item in lista_csv:  # Corrigido aqui
        if item["entregue"] == "True":
            lista_produtos_entregues.append(item)
            
    return lista_produtos_entregues   


def soma_produtos_entregues(lista_produtos_entregues: list[dict]) -> int:
    valor_soma = 0
    for item in lista_produtos_entregues:
        valor_soma += float(item["price"])
        
    return valor_soma

itens_vendas = ler_csv(csv_arquivo)
print(itens_vendas)

produtos_entregues = filtrar_produtos_entregues(itens_vendas)
print(produtos_entregues)

valor_total_entregues = soma_produtos_entregues(produtos_entregues)
print(valor_total_entregues)

valor_total = soma_produtos_entregues(itens_vendas)
print(valor_total)