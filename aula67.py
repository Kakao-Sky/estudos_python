# Valores padrão para parâmetros de funções
# Ao definir uma função, os parâmetros podem ter valores padrão.
# Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
# Refatorar: editar o seu código
# Todo parâmetro que vem depois de um parâmetro que tem valor padrão, precisa ter um valor parão também

def soma(x, y, z=None): # se o valor padrão de z fosse 0, ia sempre aparecer que ele era falso, 
    #por isso usar o None
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(2, 3)
soma(4, 5, 0)
soma(7, 5, 4)