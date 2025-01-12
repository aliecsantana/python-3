"""
Operador lógico "or": 
A expressão será verdadeira se pelo menos uma das condições for verdadeira. Se um valor verdadeiro for encontrado, a avaliação para e retorna aquele valor.
"""

entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' or entrada == 'e' and senha_digitada == senha_permitida:
    print('Acesso permitido. Bem-vindo!')
else:
    print('Acesso negado.')

# Avaliação de curto-circuito: a avaliação para no primeiro valor verdadeiro encontrado
print(True or False or 0)