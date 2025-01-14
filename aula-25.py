"""
Interpolação de strings:
- %s: string;
- %d ou %i: inteiro;
- %f: float;
- %x ou %X: hexadecimal (ABCDEF0123456789).
"""

# Exemplo com uma variável
nome = 'Ana'
mensagem_uma_variavel = 'Seja bem-vinda, %s!' % nome
print(mensagem_uma_variavel)

# Exemplo com mais de uma variável
produto = 'notebook'
preco = 2500.75
mensagem_duas_variaveis = 'O %s custa R$%.2f.' % (produto, preco)
print(mensagem_duas_variaveis)