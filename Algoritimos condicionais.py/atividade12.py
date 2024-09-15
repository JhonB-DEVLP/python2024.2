# Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 
# 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento

identificacao = input("Digite o número de identificação do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
media_exercicios = float(input("Digite a média dos exercícios do aluno: "))

media_aproveitamento = (nota1 + (nota2 * 2) + (nota3 * 3) + media_exercicios) / 7

if media_aproveitamento >= 90:
    conceito = "A"
    mensagem = "Aprovado"
elif media_aproveitamento >= 75:
    conceito = "B"
    mensagem = "Aprovado"
elif media_aproveitamento >= 60:
    conceito = "C"
    mensagem = "Aprovado"
elif media_aproveitamento <= 40:
    conceito = "D"
    mensagem = "Reprovado"
else: 
    conceito = "E"
    mensagem = "Reprovado"
    
print(f"Número de identificação do aluno: {identificacao}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos exercícios: {media_exercicios:.2f}")
print(f"Média de aproveitamento: {media_aproveitamento:.2f}")
print(f"Conceito: {conceito}")
print(f"Resultado: {mensagem}")