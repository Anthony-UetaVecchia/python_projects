# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
numeros_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Jonathan', 'Joseph', 'Jotaro', 'Josuke']
anos = [2006, 2024]

# 2 - Crie uma lista e utilize um loop for para 
# percorrer todos os elementos da lista.
stands = ['The World', 'Star Platinum', 'Crazy Diamond', 'Killer Queen']
for stand in stands:
    print(f'- {stand}')

# 3 - Utilize um loop for para calcular a soma dos
# números ímpares de 1 a 10.
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
    print(soma_impares)

# 4 - Utilize um loop for para imprimir os números
# de 1 a 10 em ordem decrescente.
for i in range(10, 0, -1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida,
# utilize um loop for para imprimir a tabuada desse 
# número, indo de 1 a 10.
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

# 6 - Crie uma lista de números e utilize um loop
# for para calcular a soma de todos os elementos.
# Utilize um bloco try-except para lidar com 
# possíveis exceções.
numeros_6 = [12, 3, 2, 32]
soma = 0
try:
    for numero in numeros_6:
        soma += numero
    print(f'Soma dos números: {soma}')
except Exception as e:
    print(f'Ocorreu um erro {e}')

# 7 - Construa um código que calcule a média dos
# valores em uma lista. Utilize um bloco try-except
# para lidar com a divisão por zero, caso a lista
# esteja vazia.
numeros_7 = [1, 3, 7, 2, 4]
soma = 0
try:
    for numero in numeros_7:
        soma += numero
    media = soma / len(numeros_7)
    print(f'Média dos valores: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média')
except Exception as e:
    print(f'Ocorreu um erro: {e}')