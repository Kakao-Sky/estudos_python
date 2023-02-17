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

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    tarefas.append(tarefa)




tarefas = []
tarefas_refazer = []

while True:
    print('Comandos aceitos: listar, desfazer, refazer')
    tarefa = input("Digite uma tarefa ou comando: ")

    if tarefa == 'listar':
        listar(tarefas)
        print()
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        print()
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        print()
        continue
    else:
        adicionar(tarefa, tarefas)
        print()
