'''
criar variáveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
criar variáveis com o ano atual (int)
obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
'''

nome  = 'Lucian'
idade = 33
altura = 1.8
peso = 77.0
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu  em {nascimento}.')
