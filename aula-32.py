numero = input('Digite um número inteiro: ')

if numero.lstrip('-').isdigit(): # Verifica se a string, ignorando o sinal negativo, contém apenas dígitos (0-9)
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0:
        print('Ele é um número par.')
    else:
        print('Ele é um número ímpar.')
else:
    print('Ele não é um número inteiro.')


hora = input('Que horas são (0-23)? ')

if hora.lstrip('-').isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Por favor, digite um número entre 0 e 23.')
    elif hora <= 11:
        print('Bom dia!')
    elif hora <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')
else:
    print('Por favor, digite apenas números inteiros.')


nome = input('Digite o seu nome: ').strip() # .strip() remove espaços extras

if len(nome) <= 4 :
    print('Seu nome é curto.')
elif len(nome) <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito longo.')