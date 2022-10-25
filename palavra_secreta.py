palavra = 'morango'
digitadas = []
chances = 3

while True:
    if chances == 0:
        print('Suas chances acabaram... Voce perdeu')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('-='*30)
        print('AHH não vale... por favor, digite apenas uma letra.')
        print('-='*30)
    else:
        digitadas.append(letra)
       
    if letra in palavra:
        print('-='*30)
        print(f'MUITO BEMMMM!! A LETRA "{letra}" ESTÁ NA PALAVRA SECRETA!!')
        print('-='*30)
    else:
        print('-='*30)
        print(f'QUE PENA! A LETRA "{letra}" NÃO ESTÁ NA PALAVRA SECRETA... TENTE OUTRA VEZ.')
        print('-='*30)
        digitadas.pop
    secreta_temp = ''
    for letra_sec in palavra:
        if letra_sec in digitadas:
            secreta_temp += letra_sec
        else:
            secreta_temp += '*'
    if palavra == secreta_temp:
        print(f'PARABÉNS!!!! VOCE ACERTOU TODA PALAVRA "{secreta_temp}"')
        break
    else:
        print(f'TOTAL DESCOBERTO DA PALAVRA: {secreta_temp}')

    if letra not in palavra:
        chances -= 1
    print(f'Voce ainda possui {chances}')
    print()
        
        


