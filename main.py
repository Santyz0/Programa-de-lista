import os

lista = []

while True:
    entrada =  (input('Selecione como você quer interagir com a lista \n [i]nserir [l]istar [a]pagar: '))

    if entrada == 'i':
        os.system('cls')
        valor_inserido = input('Adicione um item para sua lista: ')
        lista.append(valor_inserido)

    elif entrada == 'l':
        os.system('cls')

        if len(lista) == 0:
            print ('Sua lista esta vazia')
            continue
        for i, valor_inserido in enumerate(lista):
            print(i, valor_inserido)
    elif entrada == 'a':
        valor_apagadoSTR = input('Digite o indice que você quer apagar: ')

        try:
            valor_apagado = int(valor_apagadoSTR)
            del lista[valor_apagado]
        except ValueError or IndexError:
            print ('Coloque um valor existente!')
        
    else:
        print ('Esse valor não esta entre os sugeridos \n Escolha entre "i" "a" "l"')    





