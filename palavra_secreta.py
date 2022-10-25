from time import sleep
palavra = 'morango'
digitadas = []
chances = 3

print('=-'*30)
sleep(2)
print('\033[1;34;40mBEM VINDO AO JOGO DA PALAVRA SECRETA\033[m')
sleep(2)
print('\033[1;34;40mVOCE TEM 3 CHANCES PARA DESCOBRIR QUAL É A PALAVRA SECRETA...\033[m')
print('\033[1;34;40mDIGITE UMA LETRA POR VEZ\033[m')
print('=-'*30)
while True:
    if chances == 0:
        print('\033[1;31;40mSuas chances acabaram... Voce perdeu\033[m')
        print(f'\033[1;31;40mA palavra secreta era {palavra}\033[m')
        print(f'\033[1;31;40mGAME OVER!! {palavra}\033[m')
        break
    letra = input('\033[1;34;40mDigite uma letra: \033[m')
    if len(letra) > 1:
        sleep(2)
        print('-='*30)
        print('\033[1;33;40mAHH não vale... por favor, digite apenas uma letra.\033[m')
        print('-='*30)
    else:
        digitadas.append(letra)
       
    if letra in palavra:
        sleep(2)
        print('-='*30)
        print(f'\033[1;32;40mMUITO BEMMMM!! A LETRA "{letra}" ESTÁ NA PALAVRA SECRETA!!\033[m')
        print('-='*30)
    else:
        sleep(2)
        print('-='*30)
        print(f'\033[1;31;40mQUE PENA! A LETRA "{letra}" NÃO ESTÁ NA PALAVRA SECRETA... TENTE OUTRA VEZ.\033[m')
        print('-='*30)
        digitadas.pop
    secreta_temp = ''
    for letra_sec in palavra:
        if letra_sec in digitadas:
            secreta_temp += letra_sec
        else:
            secreta_temp += '*'
    if palavra == secreta_temp:
        sleep(2)
        print(f'\033[1;32;40mPARABÉNS!!!! VOCE ACERTOU TODA PALAVRA "{secreta_temp}"\033[m')
        break
    else:
        sleep(2)
        print(f'\033[1;34;40mTOTAL DESCOBERTO DA PALAVRA: {secreta_temp}\033[m')

    if letra not in palavra:
        chances -= 1
    sleep(2)
    print(f'\033[1;34;40mVoce ainda possui {chances}\033[m')
    print()
    print('~'*60)
    print()
        
        


