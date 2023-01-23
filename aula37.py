"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim 

"""

contador = 0
while contador <= 100:
    contador += 1 

    if contador == 6:
        print("Num mostro")
        continue

    if contador >= 10 and contador <= 27:
        print('num mostro o ', contador)
        continue
    print(contador)

    if contador == 100:
        break

print("a-ca-bou")
