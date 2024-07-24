# 1 - Crie um dicionário representando informações 
# sobre uma pessoa, como nome, idade e país.
pessoa = {'nome':'Giorno Giovanna', 'idade':17, 'pais':'Itália'}

# 2 - Utilizando o dicionário criado no item 1:
# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
pessoa['idade'] = 15
pessoa['profissão'] = 'Mafioso'
del pessoa['pais']
print(pessoa)

# # 3 - Crie um dicionário utilizando para representar
# # números e seus quadrados de 1 a 5.
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# # 4 - Crie um dicionário e verifique se uma chave
# # específica existe dentro desse dicionário.
livro = {
    'titulo': 'Aprendendo Python',
    'autor': 'Fabrício Silva',
    'ISBN': '12345',
    'preco': 59.90,
    'em_estoque': True
}
if 'autor' in livro:
    print("A chave 'autor' existe no dicionário.")
else:
    print("A chave 'autor' não existe no dicionário.")

# # 5 - Escreva um código que conte a frequência de
# # cada palavra em uma frase utilizando um dicionário.
# frase = 'Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos.'
contagem_palavras = {}
palavras = contagem_palavras.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)