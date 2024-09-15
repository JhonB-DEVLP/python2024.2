# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente. 
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

valores = [valor1, valor2, valor3]

if len(set(valores)) == 3:
    valores.sort(reverse=True)
    
    print(f"Os valores em ordem decrescente:", valores)
else:
    print("Os valores devem ser diferentes.")