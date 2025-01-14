"""
Formatação básica de strings em Python:
1. Especificadores de tipo:
   - "s": string;
   - "d": inteiro (decimal);
   - "f": número de ponto flutuante;
   - ".numero_f": define o número de casas decimais para floats;
   - "x" ou "X": número em formato hexadecimal.
2. Alinhamento e preenchimento:
   - ">": alinha à direita;
   - "<": alinha à esquerda;
   - "^": centraliza o texto;
   - "=": força o sinal a aparecer antes dos zeros em números.
3. Controle de sinais:
   - "+": mostra sempre o sinal ("+" ou "-);
   - "-": mostra apenas o sinal negativo.
4. Conversion flags:
   - "!r": representação interna (usando "repr");
   - "!s": representação como string (usando "str");
   - "!a": representação ASCII.
"""

variavel = "ABC"

# Exibe a variável sem alterações
print(f"{variavel}")

# Alinha à direita com 10 caracteres
print(f"{variavel: >10}") 

# Alinha à esquerda com 10 caracteres
print(f"{variavel: <10}")

# Centraliza a string com 10 caracteres
print(f"{variavel: ^10}")

# Formata o número com 1 casa decimal, preenchido com zeros à esquerda, sinal (+), largura 10 e separador de milhar
print(f"{1000.4873648123746:0=+10,.1f}") # No terminal: +0001,000.5

# Exibe o número hexadecimal com largura 8, preenchido com zeros à esquerda
print(f"{1500:08X}") # No terminal: 000005DC

# Exibe a representação interna da variável usando repr (ideal para depuração)
print(f"{variavel!r}") # No terminal: 'ABC'