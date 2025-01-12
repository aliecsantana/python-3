"""
Python é uma linguagem de programação com tipagem dinâmica e forte;
Strings são textos que estão delimitados por aspas simples ('') ou duplas ("").
"""

# Exemplo de impressão sem string
print(1234)

# Aspas simples: útil quando o texto não contém aspas simples dentro dele
print('Alice Santana')
print(1, 'Alice "Santana"')  # Aspas duplas podem ser usadas dentro de aspas simples sem problemas

# Aspas duplas: útil quando o texto contém aspas simples dentro dele
print("Alice Santana")
print(2, "Alice 'Santana'")  # Aspas simples podem ser usadas dentro de aspas duplas sem problemas

# Escape: o caractere de barra invertida (\) permite incluir aspas no texto sem causar erro
print("Alice \"Santana\"")  # Aqui as aspas duplas são escapadas com \ para serem exibidas no texto

# r: O prefixo 'r' transforma a string em "raw string" (string literal), isso significa que os caracteres de escape (como \) são tratados como texto comum
print(r"Alice \"Santana\"")  # Aqui o \ é exibido literalmente, sem escapar as aspas