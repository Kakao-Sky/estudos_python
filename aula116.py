# Criando arquivos com Python
# Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha) - protocolo - já abre e fecha o arquivo independente de qualquer coisa
# Métodos úteis:
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# módulo os:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
import os

# módulo json:
# json.dump - Gera um arquivo json
# json.load

# # caminho geralmente relativo ao arquivo atual
# caminho_arquivo = '/home/gdppi/Documentos/estudos_python_carol/'
# caminho_arquivo += 'aula116.txt' # procura esse arquivo dentro da pasta em que o código está localizado

# criando um arquivo
# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# # Criando um arquivo com o context manager
caminho_arquivo = 'aula116.txt' # o arquivo será criado na mesma pasta em que estou
# with open(caminho_arquivo, 'w') as arquivo: # 'w' é escrita e pode ser usado para criar o arquivo
#     arquivo.write('Linha 1 \n')
#     arquivo.write('Linha 2 \n')
#     arquivo.write('Estou escrevendo no arquivo pelo código \n')

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())


# with open(caminho_arquivo, 'w+') as arquivo: # 'w' é escrita com possibilidade de leitura
#     arquivo.write('Linha 1 \n')
#     arquivo.write('Linha 2 \n')
#     arquivo.writelines(('Linha 3\n', 'Linha 4\n')) # escrevendo mais de uma linha
#     arquivo.write('Estou escrevendo de novo e vou poder ler ele aqui mesmo \n')
#     arquivo.seek(0, 0) # definindo que o cursor vai estar inicialmente no começo do arquivo
#     print(arquivo.read())
#     print('lendo')
#     arquivo.seek(0, 0) # movendo o cursor novamente para o começo do arquivo
#     # print(arquivo.readline()) # lê uma linha do arquivo (é como se fosse um 'next')
#     # print(arquivo.readline())
#     # print(arquivo.readline(), end='')
#     # print(arquivo.readline().strip())
#     # print(arquivo.readline())
#     for linha in arquivo.readlines(): # readlines -> todas as linhas do arquivo
#         print(linha.strip())

with open(caminho_arquivo, 'w+') as arquivo: 
    arquivo.write('atenção \n') # write vai apagar o que tinha no arquivo e escrever essas coisas
    arquivo.write('linha 2 \n')
    arquivo.writelines(('linha 3\n', 'linha 4\n'))

# os.remove(caminho_arquivo) # unlink faz a mesma coisa
os.rename(caminho_arquivo, 'aula116-2.txt')
