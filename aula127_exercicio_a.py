# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias
# da classe com os dados salvos.
# Faça isso em arquivos separados


# MINHA SOLUÇÃO

# import json

# caminho_arquivo = 'aula127.json'
# def salvar(dados_dict, caminho_arquivo):
#     dados = dados_dict
#     with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
#         dados = json.dump(dados, arquivo, indent=2, ensure_ascii=False)
#     return dados

# class Pessoa:
#     ano_atual = 2023
    
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def get_ano_nascimento(self):
#         return Pessoa.ano_atual - self.idade

# p1 = Pessoa('João', 35)
# p2 = Pessoa('Carol', 40)

# salvar(vars(p1), caminho_arquivo)
# # salvar(vars(p2), caminho_arquivo)

# solução do PROFESSOR
import json
CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Lucas', 13)
p3 = Pessoa('Clara', 18)

base_dados = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(base_dados, arquivo, ensure_ascii=False, indent=2)
