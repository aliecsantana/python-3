nome = 'Alice'
altura_em_metros = 1.68 
peso_em_kg = 57
imc = peso_em_kg / altura_em_metros ** 2

# Exibindo o resultado com f-strings e formatando o número para duas casas decimais
print(f'O IMC de {nome} é: {imc:.2f}.')