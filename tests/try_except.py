
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while nome_valido == False:
    try:
        nome_usuario: str = input("Digite seu nome: ")
        
        if len(nome_usuario) == 0:
            raise ValueError("O nome não pode ser vazio")
        elif any(i.isdigit() for i in nome_usuario):
            raise ValueError("O nome não pode conter números")
        else:
            print(f"Seu nome é {nome_usuario}")
            nome_valido = True
    except ValueError as e:
        print(e)
    
while salario_valido == False:
    try:
        salario_usuario: float = float(input("Digite seu salário: "))
        if salario_usuario <= 0:
            raise ValueError("O salário não pode ser menor ou igual a zero")
        else:
            print(f"Seu salário é {salario_usuario}")
            salario_valido = True
    except ValueError as e:
        print(e)

while bonus_valido == False: 
    try:
        bonus_usuario: float = float(input("Digite a porcentagem do bônus recebido: "))
        if bonus_usuario <= 0:
            raise ValueError("O bônus não pode ser menor ou igual a zero")
        elif bonus_usuario > 100:
            raise ValueError("O bônus não pode ser maior que 100%")
        else:
            bonus_valido = True
            bonus_final = salario_usuario + salario_usuario * bonus_usuario/100
            print(f"Seu bônus é {bonus_final}")
    except ValueError as e:
        print(e)