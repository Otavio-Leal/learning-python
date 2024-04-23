
texto = "hoje eh nosso segundo bootcamp, bootcamp de python"

texto = texto.replace(",","")
palavras = texto.split()


print(palavras)

contagem_palavras = {}

for i in palavras:
    if i in contagem_palavras:
        contagem_palavras[i] += 1
    else:
        contagem_palavras[i] = 1
        
print(contagem_palavras)