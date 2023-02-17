# Evitando o uso de condicionais + Guard Clause

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

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    # lambda tá adiando a execução da função
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']

    comando()



    # if tarefa == 'listar':
    #     listar(tarefas)
    #     print()
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     print()
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     print()
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     print()
