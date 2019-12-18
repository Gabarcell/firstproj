from televisao import Televisao

def sair():  # SAIR <<<<<<<<
    print('-' * 45)
    choice = input('TEM CERTEZA QUE DESEJA SAIR DO MENU: [S/N] ').upper()
    if choice == 'N':
        print('')
        return mainMenu()
    elif choice == 'S':
        print('')
        print('-' * 45)
        print('               DESLIGANDO TV... ')
        print('             - - - - - - - - - - ')
        print('              \033[1;31mD E S L I G A D A\033[0m')
        print('-' * 45)
        exit()
    else:
        print('-' * 45)
        print('               SOMENTE [S/N]')
        print('-' * 45)
        return sair()
def mainMenu():
    print('-'*45)
    print('               \033[34mM   E   N   U\033[0m')
    print('-'*45)

    print('TECLE |A| para LIGAR: ')
    print('TECLE |B| para DESLIGAR: ')
    print('TECLE |C| para DIGITAR VOLUME: ')
    print('TECLE |D| para AUMENTAR VOLUME: ')
    print('TECLE |E| para DIMINUIR VOLUME: ')
    print('TECLE |F| para MUDO: ')
    print('TECLE |G| para SAIR MUDO: ')
    print('TECLE |H| para DIGITAR CANAL: ')
    print('TECLE |I| para AUMENTAR CANAL: ')
    print('TECLE |J| para DIMINUIR CANAL: ')
    print('TECLE |K| para TOCAR: ')
    print('TECLE |KK| para DESLIGAR TOCAR: ')
    print('TECLE |L| para DISPLAY:')
    print('TECLE |M| para SAIR: ')
    print('-'*45)


    while True:
        try:
            choose = str(input('Digite a opção escolhida do menu: ')).upper()
            if choose == 'A':
                tv.ligar()
            elif choose == 'B':
                tv.desligar()
            elif choose == 'C':
                tv.escolher_Volume()
            elif choose == 'D':
                tv.aumentar_Volume()
            elif choose == 'E':
                tv.diminuir_Volume()
            elif choose == 'F':
                tv.mudo()
            elif choose == 'G':
                tv.tirarMudo()
            elif choose == 'H':
                tv.escolher_canal()
            elif choose == 'I':
                tv.trocar_Canal()
            elif choose == 'J':
                tv.diminuir_Canal()
            elif choose == 'K':
                tv.tocar()
            elif choose == 'KK':
                tv.sair_Tocar()
            elif choose == 'L':
                tv.name()
            elif choose == 'M':
                sair()
                print('-' * 45)
                print('              SAINDO DO MENU...')
                print('                  ------   ')
                print('               TV DESLIGADA')
                print('-' * 45)
                exit()
            else:
                print('-'*45)
                print('         OPÇÃO INVALÍDA, APENAS LETRAS!')
                print('-' * 45)
                return mainMenu()
        except ValueError:
            print('-'*45)
            print('             OPÇÃO INVALIDA:')
            print('-' * 45)
            mainMenu()
tv = Televisao()
mainMenu()


