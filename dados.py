def menu():
    # Função responsável pelo menu e que também irá receber e retornar a quantidade de dados que serão rolados.
    print('-' * 50)
    print('DICE ROLLER'.center(50))
    print('-' * 50)
    quant = leiaInt('Quantos dados você deseja jogar (DIGITE 0 PARAR)? ')
    return quant


def tipos(dados):
    # Mostrar os tipos de dados
    print('-' * 50)
    for i, d in enumerate(dados):
        print(f'{i + 1} - d{d}')
    print('-' * 50)
    # Loop infinito que só será encerrado caso o usúario digite um valor que não seja 0 ou não seja maior que 7.
    while True:
        # Chamando a função leiaInt.
        esc = leiaInt('Qual tipo de dado você deseja? ')
        if esc > 7 or esc == 0:
            print('ERRO! Valor inserido inválido')
            print('-' * 50)
        else:
            return esc


def leiaInt(msg):
    # Função que irá tentar ler um número inteiro, caso o valor digitado não seja inteiro ou seja menor que zero, será exibido uma mensagem de erro, caso nada disso ocorra, o valor será retornado.
    while True:
        try:
            num = int(input(msg))
        except:
            print('ERRO! Valor inserido inválido')
            print('-' * 50)
        else:
            if num < 0:
                print('ERRO! Valor inserido inválido')
                print('-' * 50)
            else:
                return num


def rolls(num, tipo):
    # Importação da função sleep e randint.
    from time import sleep
    from random import randint
    soma = 0
    # Exibição do resultado.
    print('-' * 50)
    print('RESULTADO'.center(50))
    print('-' * 50)
    print(f'{num}d{tipo}', end=' -> ', flush=True)
    sleep(0.8)
    # Loop com range igual a quantidade de dados que usúario escolheu para serem rolados.
    for c in range(1, num + 1):
        # Aqui acontece a rolagem do dado.
        face_dado = randint(1, tipo)
        # Depois o valor é adicionado a variável soma.
        soma += face_dado
        # Exibindo o valor ao usúario.
        if c != num:
            print(face_dado, end=' + ', flush=True)
            sleep(0.8)
        # Exibido o último valor e depois apresentado a soma de tudo
        elif c == num:
            print(face_dado, end=f' = {soma}', flush=True)
    print()
