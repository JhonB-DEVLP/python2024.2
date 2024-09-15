# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal deetiqueta e a escolha da condição de pagamento. 

preco_normal = float(input("Digite o preço normal de etiqueta do produto: R$ "))
condicao_pagamento = int(input("Escolha a condição de pagamento: (1 ,2, 3, ou 4): "))

if condicao_pagamento == 1:
    valor_a_pagar = preco_normal * 0.90
    print(f"Valor a ser pago à vista, dinheiro ou cheque: R$ {valor_a_pagar:.2f}")
    
elif condicao_pagamento == 2:
    valor_a_pagar = preco_normal * 0.85
    print(f"Valor a ser pago à vista no cartão de crédito: R$ {valor_a_pagar:.2f}")

elif condicao_pagamento == 3:
    valor_a_pagar = preco_normal
    print(f"Valor a ser pago em duas vezes sem juros: R$ {valor_a_pagar:.2}")

elif condicao_pagamento == 4:
    valor_a_pagar = preco_normal * 1.10
    print(f"Valor a ser pago em duas vezes sem juros: R$ {valor_a_pagar:.2f}")
else: 
    print("Código de condição de pagamento inválido!")