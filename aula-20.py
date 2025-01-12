# Solicita ao usuário para digitar dois valores e armazena cada um deles
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# Compara os dois valores e exibe qual é maior ou igual
if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual 'f'a {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior 'f'que {primeiro_valor=}')