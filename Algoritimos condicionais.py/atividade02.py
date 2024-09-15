# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). 
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").strip().upper()
estadoCivil = input("Digite o estado civil solteiro(a), casada(a), divorciada(a), viúva(a): ").strip().upper()

if sexo == "F" and estadoCivil == "CASADA":
    tempoCasada = int(input("Digite o seu tempo de casada em anos: "))
    print (f"{nome} está casa há {tempoCasada} anos. ")
else: 
    print (f"{nome}, seus dados foram registrados com sucesso.")