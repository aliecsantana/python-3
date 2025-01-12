"""
Operadores "in" e "not in":
- "in": Verifica se um valor está presente em uma sequência (como strings, listas, etc.);
- "not in": Verifica se um valor NÃO está presente em uma sequência.

Strings são iteráveis, e cada caractere de uma string possui um índice.
Exemplo:
    Índices positivos:  0  1  2  3  4  
                        A  l  i  c  e  
    Índices negativos: -5 -4 -3 -2 -1
"""

nome = 'Alie'
print(nome[2])
print('z' in nome) # Verifica se a letra "z" está entre os caracteres da variável "nome" e retorna "True" ou "False"