condicao_1 = True
condicao_2 = True
condicao_3 = True
condicao_4 = True

# Verifica a condição 1, executa o código se for verdadeira
if condicao_1:
    print('Processando dados da condição 1.')
    print('Executando ação relacionada à condição 1.')

# Se a condição 1 não for verdadeira, verifica a condição 2
elif condicao_2:
    print('Processando dados da condição 2.')

# Se as condições anteriores não forem verdadeiras, verifica a condição 3
elif condicao_3:
    print('Processando dados da condição 3.')

# Se nenhuma das condições anteriores for verdadeira, verifica a condição 4
elif condicao_4:
    print('Processando dados da condição 4.')

# Se nenhuma condição for verdadeira, executa o código do else
else:
    print('Nenhuma condição foi satisfeita. Nenhuma ação será realizada.')

# Verifica se 10 é igual a 10 (sempre verdadeiro)
if 10 == 10:
    print('Condição adicional verificada: 10 é igual a 10')

# Código que está fora dos blocos condicionais
print('Fim da execução.')