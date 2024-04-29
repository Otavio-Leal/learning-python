import csv

path: str = "tests/test.csv"

lista_csv: list = []

with open(file=path, mode="r", encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        lista_csv.append(row)
        
print(lista_csv) 