import os


carros = [
    ("Chevrolet Tracker", 120),
    ("Jeep Renegade", 180),
    ("Jeep Commander", 280),
    ("Chevrolet Onix", 100),
    ("Hyundai HB20", 100),
    ("HyundaiTucson", 200),
    ("FIat Pulse", 170),
    ("FIat Uno", 70),
    ("FIat Chronos", 120)
          ]
alugados = []



print("=======")
print("Bem vinda a Locadora de Carro do Clayton")
print("=======")

def mostrar_lista_de_carros(lista_de_carros): 
    for i, car in enumerate(lista_de_carros): 
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))



while True: 
    os.system("clear")
    print("=======")
    print("Bem vindo a Locadora de Carro do Clayton")
    print("=======")

    print("O que está procurando?")
    print("0 - Mostrar Portifólio de Carros | 1 - Alugar um carro | 2 - Devolucao de Carro Alugado")
    op = int(input())

    os.system ("clear")
    if op == 0:
        mostrar_lista_de_carros(carros)

    elif op == 1: 
        mostrar_lista_de_carros(carros)
        print("========")
        print("Escolha o código do carro que deseja alugar: ")
        cod_car = int(input())
        print("Por quantos dias você deseja alugar este carro? ")
        dias = int(input())
        os.system("clear")

        print("Você escolheu {} por {} dias.".format(carros[cod_car][0], dias))
        print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * carros[cod_car][1]))

        print("0 - SIM | 1 - NAO")
        conf = int(input())
        if conf == 0:
            print("Oarabéns você alugou o {} por {} dias.".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0: 
            print("VNão possui carros a serem devolvidos.") 
        else:
            print("========")
            print("Segue a lista de carros alugados. Qual você deseja devolver? ")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver: ")
            cod = int(input())
            if conf == 0: 
                print("Obrigado por devolver o carro {}".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))


    print("")
    print("======")
    print("Escolha uma das Opçoes Digitando")
    print("0 - CONTINUAR | 1 - SAIR")

    if float(input()) == 1:
        break




