'''
CONSTANTE = "variáveis" que não vão mudar 
    - não existe no python
    - usar letras maiúsculas por convenção
muitas condições no mesmo if (ruim) -> contagem de complexidade (ruim)

'''

velocidade = 70     # velocidade atual do carro
local_carro = 99   # local do carro na estrada

RADAR_1 = 60        # velocidade máxima do radar 1
LOCAL_1 = 100       # local onde está o radar 1
RADAR_RANGE = 1     # a distância que o radar pega

if velocidade > RADAR_1:
    print("Velocidade carro passou do radar 1")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print("Carro multado no radar 1")


# simplificando

v_carro_passou_radar1 = velocidade > RADAR_1
carro_multa_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if carro_multa_radar1 and v_carro_passou_radar1:
    print("Carro multado no radar 1")