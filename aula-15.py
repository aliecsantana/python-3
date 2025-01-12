# Solicita ao usuário que insira dois números e armazena-os como strings através da função input
numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

# Converte as strings de entrada para inteiros
int_numero1 = int(numero1)
int_numero2 = int(numero2)

print(f'A soma dos números é {int_numero1 + int_numero2}.')