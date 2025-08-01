import random
from Biblio import input_int

'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1():
    lista = []
    for _ in range(15):
        lista.append(random.randrange(100))
    print(lista)
    numero = int(input_int('Digite um número a ser buscado: ',0,100))
    try:
        posicao = lista.index(numero)
    except ValueError:
        print(f'{numero} não localizado na lista')
    else:
        print(f'Localizado na posição: {posicao}')

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.
def q2():
    letras = []
    for _ in range(10):
        letras.append(chr(random.randrange(65,91)))
    cont = 1
    for c in letras:
        print(f'{cont}: {c}')
        cont+=1

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)

def q21():
    qtde = input_int('Qtde de caracteres para a senha: ',8,20)
    senha = ''
    for _ in range(qtde):
        senha += int(random.randint(40, 126))
    print(f'Senha sugerida: {senha}')


#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q3():

    numeros = []

    for i in range(15):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    print("\nNúmeros armazenados:")
    for i, num in enumerate(numeros, start=1):
        tipo = "par" if num % 2 == 0 else "ímpar"
        print(f"{i}. {num} → {tipo}")
def q35():
    arquivo = open('q3.csv', 'r')
    for linha in arquivo:
        numeros = linha.split(';')
        resultado = ''
        for numero in numeros:
            resultado+=f'{numero}\t{"PAR" if int(numero)%2==0 else "IMPAR"}\n'
        arquivo_saida = open('questao3.out','w')
        arquivo_saida.write(resultado)
    arquivo.close()
    arquivo_saida.close()#
    
#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q4():
    num = [] 
    cont = 0
    for _ in range(8):
        num.append(random.randrange(100))
    print(num)
    for n in num:
        if n % 6 == 0:
            cont += 1

    print("Quantidade de múltiplos de 6:", cont)





#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q5():
    nomes = ["Edu", "marcos", "cleber", "joao"]
    notas = [8,7,9,10]
    notas2 = [3,7,8,2]
    media = []

    for x in range(4):
        media.append( notas[x] + notas2[x]/2)
        if media >= 6 :
            print("Aprovado")
        else :
            print("Reprovado")
















#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.


#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%

def q7():
    arquivo = open('q7.csv', 'r')
    produtos = []
    l_10 = 0
    l_10_20 = 0
    l_20 = 0
    res = ''
    for linha in arquivo:
        dados = linha.split(';')
        produto = dict()
        produto['nome'] = dados[0]
        produto['compra'] =float (dados[1])
        produto['venda'] = float(dados[2])
        produto['lucro'] =  produto['venda'] /produto['compra'] -1
        produtos.append(produto)
        l_10 += 1 if produto['lucro'] < 0.1 else 0;
        l_10_20 += 1 if produto['lucro'] > 0.1 and produto['lucro'] <= 0.2 else 0;
        l_20 += 1 if produto['lucro'] > 0.2 else 0;
    arquivo.close()


    print(f'Lucro < 10%: {l_10}')
    print(f'Lucro entre 10% e 20%: {l_10_20}')
    print(f'Lucro > 20%: {l_20}')




#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.


#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.
def q14():
    numeros = [random.randint(0,50) for _ in range(50)]
    print(numeros)
    resultado = []
    for num in numeros:
        num = num * num
        resultado.append(num)
    print(resultado)
#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.
def q18():
    numeros = sorted([random.randint(0,50) for _ in range(20)])
    unicos_ordenados = sorted(set(numeros))
    
    print("Lista original:", numeros)
    print("Lista ordenada sem repetidos:", unicos_ordenados)


#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.


questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')