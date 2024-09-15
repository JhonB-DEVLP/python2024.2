#Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = numero + 5
else:
    resultado = numero + 8
    
print (f"O resultado é: {resultado}")