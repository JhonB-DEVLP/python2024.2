# Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de 
# A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

A = int(input("Digite o valor de A para calcular A!: "))

fatorial = 1 
sequencia = ""

for i in range(A, 0, -1):
    fatorial *= i
    if i > 1:
        sequencia += f"{i} x"
    else:
        sequencia += f"{i}"

print(f"{A}! = {sequencia} = {fatorial}") 