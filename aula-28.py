"""
Exercício:
1. Solicite ao usuário que digite seu nome.
2. Solicite ao usuário que digite sua idade.
3. Caso o nome e a idade sejam fornecidos:
    - Exiba:
        - "Seu nome é {nome}."
        - "Seu nome invertido é {nome invertido}."
        - "Seu nome contém (ou não) espaços."
        - "Seu nome tem {n} letras."
        - "A primeira letra do seu nome é {letra}."
        - "A última letra do seu nome é {letra}."
4. Se qualquer um dos campos (nome ou idade) for deixado vazio:
    - Exiba a mensagem: "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    
    if ' ' in nome:
        print('Seu nome contém espaços.')  
    else:
        print('Seu nome não contém espaços.')
    
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é "{nome[0]}".')
    print(f'A última letra do seu nome é "{nome[-1]}".')

else:
    print('Desculpe, você deixou campos vazios.')