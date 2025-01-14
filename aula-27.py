"""
O fatiamento de strings permite acessar partes de uma string utilizando o formato [i:f:p] ou [::], onde:
  - "i" é o início (inclusivo);
  - "f" é o fim (não inclusivo);
  - "p" é o passo (define a direção e a distância entre os índices).

A função len() retorna a quantidade de caracteres de uma string.
"""

variavel = 'Olá mundo'

# Inverte a string e imprime "odnum álO"
print(variavel[::-1])  # No terminal: odnum álO

# Realiza o fatiamento começando na posição 3, indo até a posição 0 (não inclusiva), com passo -1
print(variavel[3:0:-1])  # No terminal: ál

comprimento = len(variavel)
print(f"A string '{variavel}' tem {comprimento} caracteres.")