# Context Manager com contextlib.contextmanager
# Context Manager com função - Criando e usando gerenciadores de contexto 

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try: 
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        # yield torna a função um generator 
        yield arquivo
    # except Exception as e: 
    #     print('Ocorreu erro ', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1- \n')
    arquivo.write('Linha 2- \n')
    arquivo.write('Linha 3- \n')
    print('WITH', arquivo)