# Calcula media do aluno
n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
media = (n1 + n2) / 2
print(media)

# Estrutura de Repetição (For)
for i in range(5):
    print('Olá, estrutura de repetição.')

for i in range(5):
    print(i)

# Conta do 10 ao 20, está 21 pq é o n-1 da matematica
for i in range(10, 21):
    print(i)

# Conta um embaixo do outro
qtd = int(input('Quer contar até quanto? '))
for i in range(qtd):
    print(i)

# O end=' ' faz o resultado ficar um do lado do outro, precisa ter o espaço entre as aspas, para separar os numeros (a virgula foi só um teste)
qtd = int(input('Quer contar até quanto? '))
for i in range(qtd):
    print(i, end=', ')


# soma = 0 (não é boa prática deixar assim comentado, o normal é usar a varial como 0 mesmo fora do for.)
#  O u+1 é para a rodada começar a contar do 1 e não do 0
for u in range(3):
    print(f'\nRodada {u+1}') 
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    soma = num1 + num2 
    print(f'O total é {soma}')


# Variavel acumuladora
soma = 0
for i in range(5):
    numero = float(input('Digite um número: '))
    soma = soma + numero

print(f'O total é {soma}')


# Aqui não precisa ter o valor da venda no print do if
soma = 0
for v in range(5):
    venda = float(input('\nInforme o valor da venda: R$ '))

    if venda > 100:
        soma += venda
        print(f'Valor adicionado para somar R$ {venda}')
    else:
        print('Valor não computado')

print(f'\nTotal de R$ {soma}')




soma = 0
for v in range(5):
    venda = float(input('\nInforme o valor da venda: R$ '))

    if venda > 100:
        soma += venda
        print(f'Somando o valor.. R$ {soma}')
    else:
        print('Valor não computado')

print(f'\nTotal de R$ {soma}')
