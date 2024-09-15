# Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de 
# N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.

while True:
    N = int(input("Digite um valor para N (de 1 a 10): "))
    if 1 <= N <= 10:
        break
    else:
        print("Valor inválido! Digite um número entre 1 e 10.")

print(f"Tabuada de {N}: ")
for i in range(11):
    resultado = i * N
    print(f"{i} x {N} = {resultado}")