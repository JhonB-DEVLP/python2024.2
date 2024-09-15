# Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são VERDADEIROS ou FALSOS.
valor1 = input("Digite o primeiro valor (True/False): ").strip().capitalize() == "True"
valor2 = input("Digite o secondo valor (True/False): ").strip().capitalize() == "True"

if valor1 == valor2:
    if valor1:
        print("Ambos os valores são verdadeiros.")
    else:
        print("Ambos os valores são falsos.")
else:
    print("Os valores são diferentes")