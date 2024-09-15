#Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.
 
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros (ex: 1.75): "))

imc = peso / (altura ** 2)

if imc < 18.5: 
    condicao = "Abaixo do peso"
elif 18.5 <= imc <= 25:
    condicao = "Peso normal"
elif 25 < imc <= 30:
    condicao = "Acima do peso"
else:
    condicao = "Obesidade"

print(f"Seu IMC é: {imc:.2f}")
print(f"Condicao: {condicao}")
