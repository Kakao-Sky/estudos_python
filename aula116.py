# Criando arquivos com Python
# Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis:
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# módulo os:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# módulo json:
# json.dump - Gera um arquivo json
# json.load

# caminho geralmente relativo ao arquivo atual
caminho_arquivo = 'aula116.txt'
caminho_absoluto = '/home/gdppi/Documentos/estudos_python_carol/aula115.py'
