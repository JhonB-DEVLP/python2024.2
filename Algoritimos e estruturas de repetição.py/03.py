# Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a 
# média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores 
# negativos e o percentual de valores negativos e positivos.

soma = 0 
contador = 0
positivos = 0
negativos = 0

while True:
    valor = input("Digite um valor (ou 'Sair' para finalizar): ")
    
    if valor.lower() == 'Sair':
        break
    
    try: 
        valor = float(valor)
        
        soma += valor
        contador += 1
        
        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1
    except ValueError:
        print("Por favor digite um número válido ou 'Sair'.")
        
    if contador > 0:
        media = soma / contador
        percentual_negativos = (negativos / contador) * 100
        percentual_positivos = (positivos / contador) * 100
        
        print(f"Média aritmética dos valores lidos: {media:.2f}")
        print(f"Quantidade de valores positivos: {positivos}")
        print(f"Quantidade de valores negativos: {negativos}")
        print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
        print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
    else:
        print("Nenhum valor foi inserido.")