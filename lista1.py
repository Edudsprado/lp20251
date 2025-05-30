'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q1():
    print('Eduardo dos santos prado')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    print(30*27)


#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    print((5+8+12)/3)

#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    print = int(input("Digite um número inteiro: "))
#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    num1 = float (input("Digite um número real: "))
    num2= float (input("Digite um número real: "))
    print (num1)
    print(num2)   

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    ant = int (input("Digite um número inteiro"))
    print(ant-1)
    print(ant+1)

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = (input("DIgite seu nome:"))
    endereco = (input("Digite seu endereço"))
    tel = int(input("Digite seu telefone"))
    texto = f'''
        Nome: {nome}
        Endereço: {endereco}
        telefone: {tel}
    '''
    print(texto)
#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digitte o segundo número: "))
    print (num1-num2)


#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    num = float(input("Digite um número: "))
    print(num/4)

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    media = ((num1+num2+num3)/3)
    print(media)

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.

def q11():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1+num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    print(soma)
    print(sub)
    print(mult)
    print(div)



#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    num = float(input("Digite um número: "))
    resultado = num**2
    print(resultado)

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    num = float(input("Digite o seu saldo: "))
    print(f'Saldo com ajuste de 2%: R$ {num*1.02}')



#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).  
def q14():
    base = int(input("Digite o valor da base: ")) 
    altura = int(input("Digite o valor da altura: "))
    area1 = int(input("Digite o valor da área: "))
    perimetro = (base*2 + altura*2) 
    print(perimetro)
    area2 = (base *altura) 
    print(area2)

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    valor_produto = float(input("valor do produto : R$ "))
    porcentagem = float(input("O valor da porcetagem do desconto: "))
    valor_desconto = round(valor_produto *porcentagem/100, 2)
    valor_final = valor_produto-valor_desconto
    resultado = f'''
    valor do produto : R$ {valor_produto}
    valor do desconto ({porcentagem}%) : R$ {valor_desconto}
    valor final do produto : {valor_final}
    '''
    print(resultado)
#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    salario = float(input('Salário: '))
    percentual_reajuste = float(input('Reajuste(%): '))
    novo_salario = round(salario*percentual_reajuste/100 + salario,2)
    texto = f'''
    Salário de R$ {salario}
    com reajuste de {percentual_reajuste}%
    ficou em R$ {novo_salario}
    '''
    print(texto)

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17():
    print("COnersão de gráus para Fahrenhent")
    c = float(input('Graus: '))
    print(f'Fahrenheit: {(9 * c + 160) / 5}')


#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
    tempo_viagem = int(input('Tempo da viagem (minutos): '))/60
    velocidade_media = int(input('Velocidade Média (Km/h): '))
    distancia = tempo_viagem * velocidade_media
    litros_gastos = distancia / 12
    texto = f'''
    Duração da viagem: {int(tempo_viagem*60)} minutos ou {round(tempo_viagem,1)} horas
    Velocidade Média: {velocidade_media} Km/h
    Distância percorrida: {int(distancia)} kms
    Litros Gastos: {round(litros_gastos,1)} litros
    '''
    print(texto)

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
    valor_prestacao = float(input('Valor da Prestação: R$ '))
    taxa_juros = float(input('Taxa de Juros diária (%): '))
    dias_atraso = int(input('Qtde de dias atrasado: '))
    valor_multa = taxa_juros*dias_atraso*valor_prestacao
    texto = f'''
    Valor da Prestação: R$ {valor_prestacao}
    Taxa de Juros diária: {taxa_juros}%
    Qtde de dias de atraso: {dias_atraso} dias
    Juros a serem cobrados: {taxa_juros*dias_atraso}% = R$ {valor_multa}
    Valor final a pagar: R$ {valor_prestacao + valor_multa}
    '''
    print(texto)

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():
    print("Conversão de real para dolar")
    real = float(input("Escreva o valor que sera convertido: "))

    dolar = float(input("EScreva o cambio atual: "))

    res = real/dolar

    print(res)

questao = int (input('Questão a executar: '))
eval(f'q{questao}()')
