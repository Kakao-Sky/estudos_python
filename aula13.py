# Formatação de Strings
nome = "Caroline"
altura = 1.67
peso = 60
imc = ... # ... é usado como placeholder, o código será executado sem problemas

#imc = peso / altura ** 2 
#print(imc)

imc = peso / (altura * altura)
print(nome, ' tem ', altura, ' de altura, pesa ', peso, ' quilos, e seu IMC é ', imc)

linha_1 = f'{nome},  tem , {altura:.2f},  de altura,' #f no início dá a possibilidade de separar as variáveis com {}
# :.2f é a formatação de casas decimais
print(linha_1)
#print(...)

mensagem = f'{nome} tem {altura}  de altura, pesa {peso}  quilos e seu IMC é  {imc:.2f}'
print(mensagem)