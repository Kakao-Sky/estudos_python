# coletando dados do usuário com input()
# só recebe String, para receber outros tipos de dados, precisa fazer a coerção de dados

nome = input('Qual seu nome? ')

print(f'O seu nome é: {nome}') #{nome} no f string vai pegar o valor da variável
print(f'O seu nome é: {nome=}') #{nome=} no f string vai pegar o valor da variável e o nome da variável

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

print(f'A soma dos dois números é {num1 + num2}') 
#o resultado estará errado porque o input() só recebe str


# Uma forma de fazer sem o erro ocorrer
num1 = int(input('Digite um número: ')) #essa é uma das formas de fazer o input() receber um número
num2 = int(input('Digite outro número: ')) #ou qualquer outro tipo de dado que não seja str

print(f'A soma dos dois números é {num1 + num2}') 


#outra forma de trabalhar com números no input() é a seguinte:
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# checagem pra ver se é um número

int_num1 = int(num1)
int_num2 = int(num2)
print(f'A soma dos dois números é {int_num1 + int_num2}')
