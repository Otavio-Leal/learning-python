data = input("Insira uma data no formato dd/mm/aaaa: ")

list_data_split = data.split("/")
print (list_data_split)


ano = list_data_split[2]
mes = list_data_split[1]
dia = list_data_split[0]

print(f"A data é referente ao dia {dia} do mês {mes} do ano {ano}")