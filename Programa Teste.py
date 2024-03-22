# Solicita ao usuário que insira um número inteiro e armazena o valor em uma variável.
numero = input('Digite um numero inteiro: ')

try:
    # Tenta converter o número para inteiro.
    num = int(numero)
    
    # Verifica se o número é maior que zero.
    if num > 0:
        # Extrai os dígitos do número.
        unidade = num // 1 % 10
        dezena  = num // 10 % 10
        centena = num // 100 % 10
        milhar  = num // 1000 % 10
        
        # Imprime o número digitado.
        print(f'O Numero digitado foi {numero}')
        
        # Imprime os dígitos extraídos do número.
        print(f'Os Numeros de {num} são {milhar}, {centena}, {dezena}, {unidade}')
        
        # Calcula e imprime a soma dos dígitos do número.
        soma = unidade + dezena + centena + milhar
        print(f'A Soma dos numeros e {soma}')
        
    else:
        # Se o número for menor ou igual a zero, imprime uma mensagem.
        print(f'Voce digitou um numero menor que 0')
    

except ValueError as erro:
    # Se ocorrer um erro de valor, imprime uma mensagem de erro.
    print(f'Tivemos um erro do tipo {erro}')
