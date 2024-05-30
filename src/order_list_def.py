lista_numeros: list = [40,50,60,70,0,-23432.33]

def ordernar_lista_numeros(numeros: list):
    nova_lista_numeros = numeros.copy()
    
    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
                nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i]
                
    return nova_lista_numeros

nova_lista = ordernar_lista_numeros(lista_numeros)
print(nova_lista)
