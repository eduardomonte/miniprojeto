from operator import le


palavra = 'morango'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('-='*30)
        print('AHH não vale... por favor, digite apenas uma letra.')
        print('-='*30)
    else:
        digitadas.append(letra)
        print(digitadas)
        

