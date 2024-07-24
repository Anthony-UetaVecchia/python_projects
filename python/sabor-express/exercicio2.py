# # 1 - Solicite ao usuário que insira um número e, em seguida, 
# # use uma estrutura if else para determinar se o número é par ou ímpar.
numero_eslhido = int(input('escolha um número e direi se ele é par ou ímpar: '))
if numero_eslhido % 2 == 0:
    print('O número', numero_eslhido, 'é par\n')
else:
    print('o número', numero_eslhido, 'é ímpar\n')


# # 2 - Pergunte ao usuário sua idade e, com base nisso, use uma 
# # estrutura if elif else para classificar a idade em categorias 
# # de acordo com as seguintes condições:
# # * Criança: 0 a 12 anos;
# # * Adolescente: 13 a 18 anos;
# # * Adulto: acima de 18 anos.
idade_usuario = int(input('Quantos anos você tem? \n'))
if idade_usuario >= 18:
    print('Você é um Adulto\n')
elif 13 <= idade_usuario < 18:
    print('Você é um Adolescente\n')
else:
    print('Você é uma Criança\n')

# Caso tivesse que validar idade:
# 
# elif 0 < idade_usuario < 13:
#     print('Você é uma Criança')
# else:
#     print('Idade Inválida')


# # 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else 
# # para verificar se o nome de usuário e a senha fornecidos 
# # correspondem aos valores esperados determinados por você.
print('Cadastre-se\n')
usuario_cadastro = input('Qual será o nome do Usuário? ')
senha_cadastro = input('Qual será a senha? ')

print('\nAcesse sua conta\n')
usuario = input('Qual o nome do Usuário? ')
senha = input('Qual a senha? ')
if usuario == usuario_cadastro and senha == senha_cadastro:
    print('\nAcesso permitido\n')
else:
    raise ValueError('\nUsuário ou Senha Incorretos\n')


# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto 
# qualquer e utilize uma estrutura if elif else para determinar 
# em qual quadrante do plano cartesiano o ponto se encontra 
# de acordo com as seguintes condições:
# * Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# * Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# * Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# * Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# * Caso contrário: o ponto está localizado no eixo ou origem.
print('Me diga quais são as suas posições x e y.')
cord_x = float(input('x: '))
cord_y = float(input('y: '))
if cord_x > 0 and cord_y > 0:
    print(f'Você está no Primeiro Quadrante, nas coordenadas ({cord_x}, {cord_y})')
elif cord_x < 0 and cord_y > 0:
    print(f'Você está no Segundo Quadrante, nas coordenadas ({cord_x}, {cord_y})')
elif cord_x < 0 and cord_y < 0:
    print(f'Você está no Terceiro Quadrante, nas coordenadas ({cord_x}, {cord_y})')
elif cord_x > 0 and cord_y < 0:
    print(f'Você está no Quarto Quadrante, nas coordenadas ({cord_x}, {cord_y})')
elif cord_x == 0 and cord_y == 0:
    print('Você está na Origem')
elif cord_x == 0 or cord_y == 0:
    print('Você está no Eixo')
else:
    raise ValueError('Não é um ponto')