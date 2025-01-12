"""
Operador lógico "and":
Todas as condições precisam ser verdadeiras para que a expressão inteira seja avaliada como True. Se qualquer valor for considerado falso, a avaliação para e retorna aquele valor.

Valores considerados "falsos" (falsy) em Python:
- 0 (int), 0.0 (float), '' (string vazia), False, e None (representa a ausência de valor).
"""

entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Acesso permitido. Bem-vindo!')
else:
    print('Acesso negado.')

# Avaliação de curto-circuito: a avaliação para no primeiro valor falso encontrado
print(True and False and True)
print(True and 0 and True)