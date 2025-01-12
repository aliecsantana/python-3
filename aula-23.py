"""
Operador lógico "not":
Inverte o valor lógico de uma condição (True vira False, e vice-versa).
"""

senha_correta = "123456"
senha_digitada = input("Digite a senha: ")

if not (senha_digitada == senha_correta):
    print("Acesso negado. Senha incorreta.")
else:
    print("Acesso permitido. Bem-vindo!")