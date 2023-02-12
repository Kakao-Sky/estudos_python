# Argumentos nomeados e não nomeados (posicionais) em funções Python
# Argumento nomeado -> tem nome com sinal de igual
# Argumento não nomeado -> recebe apenas o argumento (valor)

def soma(x, y, z):
    print(f'{x=} {y=} {z=} | x + y + z= ', x + y + z)

soma(1, 2, 3) # Argumento não-nomeado
soma(y=4, x=9, z= 8) # Argumento nomeado
soma(1, 2, z = 3)  # totalmente possível, mas não poderia nomear os primeiros sem nomear os que vêm depois
soma(1, y=2, z=3)  # totalmente possível, mas não poderia nomear os primeiros sem nomear os que vêm depois

# soma(x=4, 2, 8) -> situação errada
