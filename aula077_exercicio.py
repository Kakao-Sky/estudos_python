# Exercício - Sistema de perguntas e respostas

# MINHA solução
questoes = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'], # questoes[0]
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['40', '25', '60', '55'], # questoes[1]
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['5', '3', '50', '12'], # questoes[2]
        'Resposta': '5',
    }
]

# passando pelos dicionários, que são os itens da lista
qtd_questoes = len(questoes)
acertos = 0
for questao in range(len(questoes)):
    resposta_certa = questoes[questao]['Resposta'] # armazena a resposta certa para cada pergunta
    # pra passar entre os itens dos dicionários
   
    for chave, conteudo in questoes[questao].items(): # recebe a chave e o conteúdo que estão dentro de cada dict
       
        if chave == 'Resposta': # para não mostrar a resposta
            continue
        elif chave == 'Opções':
            lista = conteudo # recebe a lista de opções
            print('Opções:')
            
            for item in enumerate(lista): # mostra os itens enumerados
                indice, opcao = item
                print(f'{indice}) {opcao}')
            
            # recebe o item da resposta correta
            resposta_do_usuario = int(input('Qual o item correto? ')) # índice das opções

            #verifica se está correta a resposta
            if(resposta_do_usuario >= len(lista)):
                print('Digite uma opção válida')
            elif (lista[resposta_do_usuario] == resposta_certa):
                print('Acertou 👍')
                acertos += 1
            else:
                print('Errou ❌') 
        else:
            print(f'{chave}: {conteudo}')

print(f'Você teve {acertos} acertos de {qtd_questoes}')

###################################################################################################
# Solução do PROFESSOR

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'], # questoes[0]
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['40', '25', '60', '55'], # questoes[1]
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['5', '3', '50', '12'], # questoes[2]
        'Resposta': '5',
    }
]

for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})',opcao)
        
    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if (escolha_int >= 0) and (escolha_int < qtd_opcoes):
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    if acertou:
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()
