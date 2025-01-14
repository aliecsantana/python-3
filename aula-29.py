"""
"try" e "except" em Python:
- "try": tenta executar o código dentro do bloco. Se não houver erros, o código é executado normalmente.
- "except": captura e trata erros que ocorrem dentro do bloco try.
"""

numero_str = input('Digite um valor e ele será dobrado: ')

# Tenta converter o valor digitado para float, calcula o dobro e exibe o resultado formatado
try: 
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') 

# Trata o caso em que a conversão para float falha
except ValueError:  
    print('Isso não é um número')