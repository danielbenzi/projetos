def calculate():
    operation = input('''
Coloque qual operacao matematica que gostaria de realizar:
+ para adicao
- para subtracao
* para multiplicacao
/ para divisao
''')

    number_1 = int(input('Coloque seu primeiro numero: '))
    number_2 = int(input('Coloque seu segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você nao colocou nenhuma operacao valida. Refaça a Operaçao novamente.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Você gostaria de realizar um novo Calculo?
Por Favor digite S para Sim e N para Nao.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até Mais.')
    else:
        again()

calculate()