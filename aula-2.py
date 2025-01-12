# Clicar em qualquer lugar da linha e pressionar Ctrl + C + Ctrl + V duplica a linha
print(10, 20)
print(30, 40)

print(50, 60, sep=",")  # 'sep' define o separador entre os valores, aqui é uma vírgula
print(70, 80, sep='|')  # O separador pode ser qualquer string

print(5, 10, sep="+", end="!!")  # 'end' substitui a quebra de linha padrão (\n) pelo texto especificado
print(15, 20, sep='-')  # Este print será exibido na mesma linha que o anterior por causa do 'end' do comando anterior

# Quando 'sep' é uma string vazia, não há separador entre os valores
print(0, 5, sep="")  
print(1, 9, sep='')

# \r\n ---> Carriage Return + Line Feed (CRLF), usado em sistemas Windows
# \n ---> Line Feed (LF), usado em sistemas Unix/Linux e no Python