"""
Flag (Bandeira) - Marca um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

"""

# por terem valores iguais, terão ids iguais
v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))

print(10 * '-')

v2 = 'b'
print(id(v1))
print(id(v2))

print(15 * '#')

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
   print('não faça')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if(passou_no_if is None):
    print('Não passou no If')
if(passou_no_if is not None):
    print('Passou no If')
