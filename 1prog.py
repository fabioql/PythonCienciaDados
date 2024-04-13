nome = input("Digite seu nome completo: ")

nome = nome.upper()

vetor_nome = nome.split(" ")


print("Primeiro nome: ", vetor_nome[0])
print('Sobrenome: ', vetor_nome[-1])