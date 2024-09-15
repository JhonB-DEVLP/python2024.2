# Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

numero = float(input("Digite um número: "))

if numero > 0:
    resultado = numero * 2
else:
    resultado = numero * 3
    
print(f"O resultado é: {resultado}")