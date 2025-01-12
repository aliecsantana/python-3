# Este programa formata variáveis em uma string utilizando "str.format()"

a = 'AAAAAA'
b = 'BBBBB'
c = 1.1

string = '{0}, {1} e {2:.2f}' # "{0}", "{1}", "{2}" são usados para referenciar os índices das variáveis fornecidas
formatacao = string.format(a, b, c) # Formata a string substituindo os placeholders pelos valores de 'a', 'b' e 'c'

print(formatacao)