# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em 
# P.A. contendo 10 valores. 

A = int(input("Digite o valor inicial de A: "))
R = int(input("Digite a razão de R: "))

print("Sequência de P.A com 10 valores: ")

for n in range(10):
    termo = A + n * R
    print(termo)