# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo['fazer café']
# refazer = todo['fazer café', 'caminhar']


# MINHA solução
lista_de_tarefas = []
desfeito = []

def inserir_na_lista(tarefa):
    lista_de_tarefas.append(tarefa)
    return 1

def desfazer_acao():
    ultimo_item = lista_de_tarefas.pop()
    desfeito.append(ultimo_item)
    return 1

def refazer_acao():
    item_refeito = desfeito.pop()
    inserir_na_lista(item_refeito)

while True:
    print('Comandos aceitos: listar, desfazer, refazer')
    entrada = input('Digite uma tarefa ou um comando: ')

    if entrada == 'listar':
        if lista_de_tarefas:
            for tarefa in lista_de_tarefas:
                print('-', tarefa)
        else:
            print('** Não há tarefas para exibir aqui **\n')
    elif entrada == 'desfazer':
        if lista_de_tarefas:
            desfazer_acao()
        else:
            print('** Não há tarefas para desfazer **\n')
    elif entrada == 'refazer':
        if desfeito:
            refazer_acao()
        else:
            print('** Não há tarefas para refazer **\n')
    elif entrada == 's':
        break
    else:
        inserir_na_lista(entrada)

    
        
# solução do PROFESSOR

