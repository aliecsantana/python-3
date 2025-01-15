"""
Uma flag é uma variável usada para indicar o estado ou o resultado de uma operação.
   
"None" representa a ausência de um valor ou um valor nulo. É frequentemente usado para inicializar variáveis cujo valor será atribuído posteriormente.

"is" e "is not" são palavras-chave utilizadas para comparar identidades de objetos. 
   - "is" verifica se duas variáveis referem-se ao mesmo objeto.
   - "is not" verifica se duas variáveis não referem-se ao mesmo objeto.

"id()" retorna a identidade única de um objeto. 
"""

condicao = False

passou_no_if = None

# Verifica a condição e define o comportamento correspondente
if condicao:
    passou_no_if = True
    print('A condição foi satisfeita. Executando ação...')
else:
    print('A condição não foi satisfeita. Nenhuma ação será tomada.')

# Verifica se a variável flag "passou_no_if" foi alterada
if passou_no_if is None:
    print('O bloco "if" não foi executado.')
else:
    print('O bloco "if" foi executado.')