# Solicita que o usuário escolha entre entrar ou sair
entrada = input('Digite "entrar" para acessar o sistema ou "sair" para finalizar: ')

# O "if" verifica a primeira condição, o "elif" avalia condições adicionais e o "else" é executado se nenhuma das anteriores for verdadeira
if entrada == 'entrar':
    print('Bem-vindo ao sistema!')
    print('Executando operações...') # Exemplo de mensagem adicional
elif entrada == 'sair':
    print('Você saiu do sistema. Até logo!')
else:
    print('Entrada inválida. Por favor, digite "entrar" ou "sair".')

# Mensagem final fora dos blocos
print('Programa encerrado.')