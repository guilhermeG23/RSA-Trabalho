#Conversor e desconversor RAS 
# Ver: 0.0.1 - Rider/Medusa - 05/10/2019 -> Inicio do projeto
# Ver: 0.0.2 - Rider/Escandor - 10/10/2019 -> Melhorias de exibicao

#Exemplos
#P : 11, Q: 13, E: 7, Inverso multiplicavel: 103
# 17, 23, 3, 235

#Entrada
print("*="*20)
entrada = str(input("Entrada do usuário: "))
print("*="*20)

#ord -> Converte caracter para decimal ascii
#chr -> Converte valor para caracter

#Saida em ascii
#Valores convertidos a ascii
array_entrada = list(entrada)
valor = len(array_entrada)
contador = 0
ascii_saida = list()
while contador < valor:
    ascii_saida.append(ord(array_entrada[contador]))
    contador = contador + 1    

print("\n")

#Chaves RSA
#Entrada com a chave publica
print("*="*20)
print("Valores das chaves")
valorP = int(input("Entre com um valor P primo: "))
valorQ = int(input("Entre com um valor Q primo: "))
#Valor N e QP
valorN = valorP * valorQ
valorPQ = (valorP - 1) * (valorQ - 1)
#Mensagem
print("\n**********************************")
print("Equacao composta de N e equacao Totiente de PQ ja estao sendo calculadas")
print("**********************************\n")
valorE = int(input("Entre com o E: "))
valorD = int(input("Inverso multiplicavel(D): "))
print("*="*20)

#Valor E
#Funcao MDC
"""
def mdc(num1, num2):
    resto = None
    while resto is not 0:
        resto = num1 % num2
        num1  = num2
        num2  = resto
    return num1
valorE = mdc(valorE, valorPQ)
print("ValorE: {} entao e {}".format(ValorE, ValorE==1))
"""

input("Em espera...")
#Valores 
print("\n")
print("*="*20)
print("Valores resultantes\nValor P: {}\nValor Q: {}\nValorN: {}\nValor PQ: {}\nValor E: {}\nValor D: {}".format(valorP, valorQ, valorN, valorPQ, valorE, valorD))
print("*="*20)

input("Em espera...")
#Formacao das chaves
print("\n")
print("*="*20)
print("Formacao das chaves")
print("Chave publica: {};{}".format(valorN, valorE))
print("Chave privada: {},{},{}".format(valorP, valorQ, valorD))
print("*="*20)

#Valor cripografado em RSA
valor = len(ascii_saida)
valor_convertido = list()
contador = 0
while contador < valor:
    valor_convertido.append(int((ascii_saida[contador] ** valorE) % valorN))
    contador = contador + 1

input("Em espera...")
#Print dos valores
print("\n")
print("*="*20)
print("Equacao para converter RSA: (valor_ascii ** valorE) % valorN")
print("*="*20)

input("Em espera...")
#Print dos valores
print("\n")
print("*="*20)
print("Saida em RSA")
print("Valor da chave em ASCII Decimal: {}".format(ascii_saida))
print("Valor da chave em RSA: {}".format(valor_convertido))
print("*="*20)

#Convertendo devolta os valores a ASCII
valor = len(valor_convertido)
valor_desconvertido = list()
contador = 0
while contador < valor:
    valor_desconvertido.append(int((valor_convertido[contador] ** valorD) % valorN))
    contador = contador + 1 

input("Em espera...")
#Print dos valores
print("\n")
print("*="*20)
print("Equacao para desconverter RSA: (valor_RSA ** valorD) % valorN")
print("*="*20)

#Convertendo valores decimais para caracteres 
valor = len(valor_desconvertido)
valor_desconvertido_rsa = list()
contador = 0
while contador < valor:
    valor_desconvertido_rsa.append(chr(valor_desconvertido[contador]))
    contador = contador + 1 

input("Em espera...")
#Valor de saida
print("\n")
print("*="*20)
print("Valor apos se desconvertida")
print("Valor em ASCII: {}".format(valor_desconvertido))
saida_final = ''.join(valor_desconvertido_rsa)
print("Valor de saida: {}".format(saida_final))
print("*="*20)

input("Em espera...")
#Valor de saida
print("\n")
print("*="*20)
print("FIM!")
print("*="*20)

