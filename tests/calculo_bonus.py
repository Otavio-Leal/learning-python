
print("\nCálculo de bonus 2022\n")

nome_usuario = input('\nDigite seu nome: \n')
salario_usuario = float(input('\nDigite seu salário: \n'))
bonus_usuario = float(input('\nDigite a porcentagem do bônus recebido: \n'))/100

bonus_final = salario_usuario + salario_usuario * bonus_usuario

print (f"\nEste é o calculo do KPI: Salário: {salario_usuario} + Bonus: {bonus_usuario*100}%\n")

print(f'\nSeu nome é {nome_usuario} e seu salário é {salario_usuario} e o valor total a receber é {bonus_final}.\n')
