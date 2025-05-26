'''
Exercícios sobre os comandos de condição em python
'''
    
from datetime import date, datetime

HOJE = datetime.now()



def exemplo_if_else():
    media = float(input('Média: '))
    if media >= 6:
        print('APROVADO')
    else:
        if media >= 3:
            print('RECUPERAÇÃO')
        else:
            print('REPROVADO')

def exemplo_if_elif_else():
    media = float(input('Média: '))
    if media >= 6:
        print('APROVADO')
    elif media >= 3:
        print('RECUPERAÇÃO')
    else:
        print('REPROVADO')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    soma = num1 + num2
    if soma > 10:
        print(f'{soma} é maior que 10')
    else:
        print(f'{soma} não é maior que 10')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    soma = num1 + num2
    if soma > 20:
        res = soma + 8
        print(f'{res} é maior que 20')
    else:
        resu = soma - 5
        print(f'{resu} não é maior que 20')

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    num1 = int(input('Digite um número: '))
    resul = (num1%3)
    if resul == 0 :
        print("É mútiplo de 3")
    else:
        print("não é mútilplo")

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
    num1 = int(input('Digite um número: '))
    resul = (num1%5)
    if resul == 0 :
        print("É mútiplo de 5")
    else:
        print("não é mútilplo de 5")

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
    num = int(input('Digite um número inteiro: '))
    if num % 3 == 0 and num % 7 == 0:
        print(f'{num} é divisível por 3 e 7')
    else:
        print(f'{num} não é divisível por 3 e 7')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q6():
    salario = int(input("Digite o valor do seu salário: "))
    prestacao = int(input("Digite o quanto pode pagar de prestação: "))
    if prestacao == 0.30*salario :
        print("O emprestimo será concedido")
    else:
        print("Valor insuficiente para emprestimo")
#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7(): 
    num1 = int(input('Digite um número: '))
    if num1 > 20 and num1 < 50 :
        print("O número está compreendido")
    else :
        print("O número não está compreendido")



#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
    num1 = int(input('Digite um número: '))
    if num1 > 20 :
        print("O número é maior que 20")
    if num1 == 20 :
        print("O numero é igual a 20")
    if num1 < 20 :
        print("O numero é menor que 20")


#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q9():
    data_str = input('Data de Nascimento (dd/mm/aaaa): ')
    data_nascimento = datetime.strptime(data_str, '%d/%m/%Y')

    if (data_nascimento > HOJE):
        print('Data inválida! Você nem nasceu ainda.')
    else:
        diferenca = HOJE - data_nascimento
        dias_totais = diferenca.days
        anos = dias_totais // 365
        dias_restantes = dias_totais % 365

        print(f'Idade: {anos} anos e {dias_restantes} dias.')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    a = int(input("O primeiro inteiro "))
    b = int(input("O segundo inteiro "))
    c = int(input("O terceiro inteiro "))

    if (a<b<c):
        print(f'{a} {b} {c}')
    if (b<a<c):
        print(f'{b} {a} {c}')
    if (c<a<b):
        print (f'{c} {a} {b}')
    if (a<c<b):
        print (f'{a} {c} {b}')
    if (b<c<a):
        print (f'{b} {c} {a}')
    if (c<b<a):
        print (f'{c} {b} {a}')

#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    a = int(input("O primeiro inteiro "))
    b = int(input("O segundo inteiro "))
    c = int(input("O terceiro inteiro "))

    if (a>b>c):
        print(f'{a} é o maior numero')
    if (b>a>c):
        print(f'{b}')
    if (c>a>b):
        print (f'{c}')
    if (a>c>b):
        print (f'{a}')
    if (b>c>a):
        print (f'{b}')
    if (c>b>a):
        print (f'{c}')

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos
def q12():
    idade = int(input("Digite a sua idade: "))
    if idade > 18 :
        print("Maior de idade ")
    if idade <= 17 :
        print("Menor de idade ")
    if idade > 65 :
        print("Idoso")
#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

def q13():
    nome = input("Digite o seu nome: ")
    not1 = int(input("Digite a nota do primeiro semestre: "))
    not2 = int(input("Digite a nota do segundo semestre: "))

    media = (not1 + not2) / 2  # Corrigido o cálculo da média

    if media > 7:
        print(f"{nome} está Aprovado")
    elif media <= 3:
        print(f"{nome} Reprovado")
    else:  # Media entre 3 e 7, então está de Prova Final
        print(f"{nome} está de Prova final")

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

def q14():
    salario = float(input("Digite seu salario: "))
    if salario <= 600:
        print("isento")
    elif (salario > 600) and (salario< 1200):
        salario = salario * 0.20
        print("O desconto será de ",salario)
    elif salario > 1200 and salario < 2000 :
        salario = salario * 0.25
        print("O desconto sera de", salario)
    elif salario > 2000 :
        salario = salario *0.30
        print("O desconto sera de", salario)

    
#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def q20():
    smed = float(input("Digite o seu saldo medio: "))
    if smed <= 500:
        print("Não possui crédito.")
    elif smed >= 501 and smed <= 1000:
        credito = smed * 0.30
        print(f"O valor do crédito é: R$ {credito:.2f}")
    elif smed >= 1001 and smed <= 3000:
        credito = smed * 0.40
        print(f"O valor do crédito é: R$ {credito:.2f}")
    else: 
        credito = smed * 0.50
        print(f"O valor do crédito é: R$ {credito:.2f}")

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
def q21():
    nome = input ("DIgite o nome do livro: ")
    name = input ("Digite seu nome: ")
    menu_usuario = '''
    [1] aluno 3 dias de empréstimo
    [2] professor 10 dias de empréstimo

    '''
    empre = int(input(menu_usuario))
    if empre == 1:
        print(f"{name}, você tem 3 dias para devolver o livro {nome} ")
    elif empre == 2:
        print(f"{name}, você tem 10 para devolver o livro {nome}")
    else:
        print("Opção invalida")
#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def q22():
    menu_carro = '''
    [1] - Tipo A (12 km/l)
    [2] - Tipo B (9 km/l)
    [3] - Tipo C (8 km/l)
    Digite o tipo de carro [1-3]
    '''

    Km = float(input("Digite o percurso em quilômetros: "))
    tipo_carro = int(input(menu_carro))

    if tipo_carro == 1:
        consumo = Km / 12
    elif tipo_carro == 2:
        consumo = Km / 9
    elif tipo_carro == 3:
        consumo = Km / 8
    else:
        print("Tipo inválido!")
        return

    print(f'O consumo estimado de combustível é:' , consumo)




#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

def q23():
    menu_prato_entrada = '''
    [1] - Vegetariano (180 kcal)
    [2] - Peixe (230 kcal)
    [3] - Frango (250 kcal)
    [4] - Carne (350 kcal)
    Digite a opção de entrada[1-4]: 
    '''
    menu_bebida = '''
    [1] - Chá (20 kcal)
    [2] - Suco de Laranja (70 kcal)
    [3] - Suco de Melão (100 kcal)
    [4] - Refrigerante Diet (65 kcal)
    Digite a opção da bebida[1-4]:
    '''
    menu_sobremesa = '''
    [1] - Abacaxi (75 kcal)
    [2] - Sorvete Diet (110 kcal)
    [3] - Mousse Diet (170 kcal)
    [4] - Mousse Chocolate (200 kcal)
    Digite a opção de sobremesa[1-4]:
    '''
    prato_entrada = int(input(menu_prato_entrada))
    bebida = int(input(menu_bebida))
    sobremesa = int(input(menu_sobremesa))

    cal = 0

    cal += 180 if prato_entrada == 1 else 0;
    cal += 230 if prato_entrada == 2 else 0;
    cal += 250 if prato_entrada == 3 else 0;
    cal += 350 if prato_entrada == 4 else 0;
    cal += 20 if bebida == 1 else 0;
    cal += 70 if bebida == 2 else 0;
    cal += 100 if bebida == 3 else 0;
    cal += 65 if bebida == 4 else 0;    
    cal += 75 if sobremesa == 1 else 0;
    cal += 110 if sobremesa == 2 else 0;
    cal += 170 if sobremesa == 3 else 0;
    cal += 200 if sobremesa == 4 else 0;

    print(f'Total de calorias do pedido: {cal} kcal')

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.
def q24():
    placa=input("DIgite a placa do carro: ")
    # Pega o último caractere da placa
    ultimo_digito = placa[-1]

    # Converte o último caractere para número inteiro
    numero = int(ultimo_digito)

    # Verifica qual é o mês de renovação conforme o número
    if numero == 1:
        mes = "Janeiro"
    elif numero == 2:
        mes = "Fevereiro"
    elif numero == 3:
        mes = "Março"
    elif numero == 4:
        mes = "Abril"
    elif numero == 5:
        mes = "Maio"
    elif numero == 6:
        mes = "Junho"
    elif numero == 7:
        mes = "Julho"
    elif numero == 8:
        mes = "Agosto"
    elif numero == 9:
        mes = "Setembro"
    elif numero == 0:
        mes = "Outubro"
    else:
        mes = "Número inválido!"

    # Mostra o mês correspondente
    print(f"O emplacamento deve ser renovado em: {mes}")


#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos



questao = int(input('Questão a executar: '))
eval(f'q{questao}()')