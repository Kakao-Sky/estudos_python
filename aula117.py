# Salvando dados Python em JSON com módulo json

import json

# pessoa = {
#     'nome': 'Caroline',
#     'sobrenome': 'Bento',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.6,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': False,
#     'nada': None,
# }

# with open('aula117.json', 'w') as arquivo:
#     json.dump(pessoa, arquivo, indent=2) # recebe um objeto e o arquivo de destino

with open('aula117.json', 'r') as arquivo:
    pessoa = json.load(arquivo) # pegando o dict de volta
    # print(pessoa)
    print(pessoa['nome'])