"""
Constantes são valores fixos que não devem ser alterados durante a execução do programa. Por convenção, são escritas em letras MAIÚSCULAS com palavras separadas por underscores (_) para facilitar a identificação.

Evite colocar muitas condições no mesmo bloco "if" para reduzir a complexidade do código e melhorar a legibilidade.
"""

# Constantes
RADAR_1_VELOCIDADE_MAXIMA = 60
RADAR_1_LOCALIZACAO = 100
RADAR_1_ALCANCE = 1

# Variáveis
carro_velocidade_atual = 61
carro_localizacao_atual = 10

# Verificações
carro_excedeu_velocidade_radar_1 = carro_velocidade_atual > RADAR_1_VELOCIDADE_MAXIMA
carro_dentro_alcance_radar_1 = (
    RADAR_1_LOCALIZACAO - RADAR_1_ALCANCE <= carro_localizacao_atual <= RADAR_1_LOCALIZACAO + RADAR_1_ALCANCE
)
carro_recebeu_multa_radar_1 = carro_excedeu_velocidade_radar_1 and carro_dentro_alcance_radar_1

# Saídas
if carro_excedeu_velocidade_radar_1:
    print("O carro está acima da velocidade permitida no radar 1.")
if carro_dentro_alcance_radar_1:
    print("O carro está dentro da área de alcance do radar 1.")
if carro_recebeu_multa_radar_1:
    print("O carro foi multado no radar 1.")