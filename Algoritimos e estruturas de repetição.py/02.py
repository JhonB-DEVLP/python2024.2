# Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar : 
# a. A menor altura do grupo; 
# b. A maior altura do grupo; 

alturas = []

for i in range(15):
    altura = float(input(f"Digite a altura da pessoa {i + 1} em metros: "))
    alturas.append(altura)

menor_altura = min(alturas)
maior_altura = max(alturas)

print(f"A menor altura do grupo é: {menor_altura:.2f} em metros")
print(f"A maior altura do grupo é Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e 
mostrar : 
a. A menor altura do grupo; 
b. A maior altura do grupo; : {maior_altura:.2f} em metros")