# Solicita ao usuário que insira duas strings
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Converte ambas as strings para letras minúsculas e divide em palavras
palavras_string1 = string1.lower().split()
palavras_string2 = string2.lower().split()

# Ordena as palavras em ordem alfabética e alfabética inversa, ignorando maiúsculas e minúsculas
palavras_string1_ordenadas = sorted(palavras_string1)
palavras_string2_ordenadas = sorted(palavras_string2, reverse=True)

# Imprime a primeira string com palavras em ordem alfabética
print("Primeira string em ordem alfabética:", ' '.join(palavras_string1_ordenadas))

# Imprime a segunda string com palavras em ordem alfabética inversa
print("Segunda string em ordem alfabética inversa:", ' '.join(palavras_string2_ordenadas))