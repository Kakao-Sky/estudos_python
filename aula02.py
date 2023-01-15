print(12, 34) #print é uma função e recebe argumentos dentro dos parênteses

"""pode receber mais de um argumento, que será separado por vírgula, em caso de 
números ou sinal de adição, em caso de textos"""

print(56, 78)

#o python já dá espaços e pula linhas automaticamente 

'''esses "espaços" são os separadores de argumentos não nomeado, é possível
modificar o separador, como mostrado abaixo:'''

# \r\n -> CRLF (quebra de fim de linha Win)
# \n -> LF (quebra de linha MAC e Lin)
print(12, 34, sep="-") #'sep=' é um argumento nomeado 
print(56, 78, sep="-")
print(9, 10, sep="-", end='\r\n')
print(11, 12, sep="-", end='\n')
print(11, 12, sep="-", end='##') #não quebra a linha, só adiciona ## ao final dela
print(11, 12, sep="-", end='\n##') #quebra a linha e adiciona ##  
print(11, 12, sep="-", end='##\n') #adiciona ## e quebra a linha
print(56, 78, sep="-")
