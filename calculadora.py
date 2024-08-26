while True:
#nessa parte eu crio as "perguntas" para o usuario de qual operador e numero ele quer que a calculadora faça o trabalho e defini os operadores permitidos na calculadora.
    numero_1 = input('Digite um numero: ')
    operador = input('Digite um operador: (+ - * /) ')
    numero_2 = input('Digite um numero: ')
    operadores_permitidos = '*-+/'
    try:
        #aqui faço a conversão dos numeros para int e ja faço a tratativas de possiveis erros.
        numero1 = int(numero_1)
        numero2= int(numero_2)
    except:
        print('Digite um numero valido')
        continue
    if len(operador) > 1:
        #aqui faço a verificação se o usuario digitou apenas 1 operador valido.
        print('Digite apenas um operador.')
        continue
    elif operador not in operadores_permitidos:
        #aqui faço a verificação se o usuario digitou algum operador não permitido
        print('Digite apenas operadores permitidos.')
        continue
    elif operador == '-':
        print('O resultado da conta é ', numero1 - numero2)
    elif operador == '+':
        print('O resultado da conta é ', numero1 + numero2)
    elif operador == '*':
        print('O resultado da conta é ', numero1 * numero2)
    elif operador == '/':
        print('O resultado da conta é ', numero1 / numero2)
    sair = input('[s]air ou [c]ontinuar ').lower().startswith('s')
    if sair is True:
        print('Você saiu.')
        break