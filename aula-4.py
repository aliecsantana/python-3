"""
Tipos:
- int: números inteiros, positivos ou negativos, incluindo o zero;
- float: números de ponto flutuante, ou seja, com casas decimais, positivos ou negativos.
"""

# Se o número não tiver um sinal, ele será considerado positivo
print(11)
print(-11)
print(0)

# O tipo float é útil para representar valores mais precisos, como medidas ou frações
print(1.1, 20.11)
print(0.0, -1.5)

# A função type() exibe o tipo de dado de uma variável ou valor literal. Ela é útil para verificar se a variável ou valor é, por exemplo, int, float ou str
print(type("Alice")) # Saída: <class 'str'>
print(type(1)) # Saída: <class 'int'>
print(type(1.1)) # Saída: <class 'float'>

# No editor de código, você pode usar Ctrl + / para comentar ou descomentar várias linhas de uma vez
# print('Esta linha está comentada e não será executada')