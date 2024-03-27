#Strings em Python

curso = 'Python Developer'

# Maiusculo, Minuscula, Titulo
print("Maiusculo: ", curso.upper())
print('Minusculo: ', curso.lower())
print('Primeira Maiuscula: ', curso.title())

#Eliminando Espaços em Branco
curso = " Python Developer "
print('Remove todos os espacos: ', curso.strip())
print('Remove espacos da Esquerda: ', curso.lstrip())
print('Remove espaco do Lado Direito: ', curso.rstrip())

#Junçao e Centralizacao
print("Centraliza: ", curso.center(10, '#'))
print('Juncao: ', ".".join(curso))