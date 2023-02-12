# https://docs.python.org/pt-br/3/library/sdtypes.html
# Tipos imutáveis vistos: str, int, float, bool 

string = "Caroline"
# string[3] = 'ABC' # não pode ocorrer, pois é imutável
print(string)

# maneira de fazer a modificação:
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)
