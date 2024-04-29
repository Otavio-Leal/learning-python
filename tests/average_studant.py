
alunos: dict = {
    "nome":  input("Digite seu nome: \n"),
    "nota":  float(input("Digite sua nota: \n"))
}

if alunos["nota"] >= 75:
    alunos["situacao"] = "Aprovado"
    
else:
    alunos["situacao"] = "Reprovado"

for k, v in alunos.items():
    print(f"{k}: {v}")
