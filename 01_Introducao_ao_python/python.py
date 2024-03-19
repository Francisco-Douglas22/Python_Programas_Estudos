
# Solicita ao usuário que insira um valor em metros
metros = float(input('Digite o valor em Metros: M '))

# Converte metros para quilômetros
km = metros / 1000

# Converte metros para hectômetros
hec = metros / 100

# Converte metros para decâmetros
deca = metros / 10

# Converte metros para decímetros
deci = metros * 10

# Converte metros para centímetros
cent = metros * 100

# Converte metros para milímetros
mili = metros * 1000

print(f'O Comprimento de {metros} Metros e equivalente a ')
print(f'''
{km} Km Quilometros
{deca} Decametros
{deci} Decimetros
{cent} Centimetros
{mili} Milimetros''')
