# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que 
# calcule seu peso ideal, utilizando as seguintes fórmulas: para homens: (72.7 * h) – 58; para mulheres: (62.1 * h) – 44.7

altura = float(input("Digite a altura em metros (ex: 1.75): "))
sexo = input("Digite o sexo (M para masculino e F para feminino): ").strip().upper()

# Cálculo do peso ideal
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com altura de {altura:.2f} m é: {peso_ideal:.2f}. kg.") 
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com altura de {altura:.2f} m é: {peso_ideal:.2f} kg.")
else:
    print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")