"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.

"""
# MINHA solução

import os

lista_compras = []

while True:
    print('Selecione uma das opções abaixo: ')
    opcao = input('[i]nserir \t [a]pagar \t [l]istar: ')
    opcoes_validas = 'ial'

    if (opcao in opcoes_validas) and (len(opcao) == 1):
        
        if(opcao == 'i'):
            os.system('cls')
            produto_inserir = input('Digite o nome do produto a ser inserido: ')
            lista_compras.append(produto_inserir)

            #print(lista_compras)
        elif opcao == 'a':
            os.system('cls')
            item_apagar_str = input('Digite o índice do produto a ser apagado: ')

            if item_apagar_str.isdigit():
                item_apagar_int = int(item_apagar_str)
                
                if item_apagar_int < len(lista_compras):
                    del lista_compras[item_apagar_int]
                    print(lista_compras)
                else:
                    print('Este item não existe dentro da lista')
            else:
                print('Digite um número, por favor')

        elif opcao == 'l':
            os.system('cls')
            print('Sua lista de compras listada: ')
            print('ÍNDICE \t PRODUTO')
            for indice, produto in enumerate(lista_compras):
                print(f'{indice} \t {produto}')
        else:
            print('Não foi possível realizar a ação')
    else:
        print('Digite uma opção válida!')


######################################################################################################
# solução do PROFESSOR

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
""" import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.') """
