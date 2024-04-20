

try:
    resultado = len("teste")
    print(resultado)
except:
    print("Não foi possível converter a string para inteiro")
else:
    print("A string foi convertida para inteiro")
finally:
    print("Conversão finalizada")