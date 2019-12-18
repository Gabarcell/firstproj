class Televisao:
    def __init__(self):                                       # CONSTRUTOR <<<<<
        self.ligada = False
        self.volume = 0
        self.canal = 0
        self.tocando = False
    def ligar(self):                                             #  LIGAR <<<
        if self.ligada == False:
            print('-'*45)
            print('                 LIGANDO TV... ')
            print('             - - - - - - - - - - ')
            print('                 \033[0;32mL I G A D A\033[0m')
            print('-'*45)
            self.ligada = True
        elif self.ligada == True:
            print('-' * 45)
            print('             TV JÁ ESTÁ LIGADA!')
            print('-' * 45)
    def desligar(self):                                            # DESLIGAR <<<
        if self.ligada == True:
            print('')
            print('-' * 45)
            print('               DESLIGANDO TV... ')
            print('             - - - - - - - - - - ')
            print('              \033[1;31mD E S L I G A D A\033[0m')
            print('-' * 45)
            self.ligada = False
        elif self.ligada == False:
            print('-' * 45)
            print('            TV JÁ ESTÁ DESLIGADA!')
            print('-' * 45)
    def aumentar_Volume(self):                                   # VOLUME   <<<<<<<<<<<<
        if self.ligada == True:
            if self.volume >= 0 and self.volume <= 190:
                self.volume += 10
                print('-'*25)
                print('       Volume + {}'.format(self.volume))
                print('-' * 25)
                return self.volume

            elif self.volume == 0:
                print('-' * 45)
                print('             Volume no MUDO!')
                print('-' * 45)
            else:
                print('-' * 45)
                print('             Volume no máximo!')
                print('-' * 45)
        else:
            print('-' * 45)
            print('PARA AUMENTAR VOLUME A TV DEVE ESTAR LIGADA!')
            print('-' * 45)
    def diminuir_Volume(self):                                # DIMINUIR VOLUME <<<<<<<<
        if self.ligada == True:
            if self.volume >= 5:
                self.volume = self.volume - 5
                print('-' * 25)
                print('       Volume  -  {}'.format(self.volume))
                print('-' * 25)

            elif self.volume == 0:
                print('-' * 25)
                print('         M U D O')
                print('-' * 25)
        else:
            print('-' * 45)
            print('PARA DIMINUIR VOLUME A TV DEVE ESTAR LIGADA!')
            print('-' * 45)
    def trocar_Canal(self):                                # SUBIR CANAL <<<<<<<<<<
        if self.ligada == True:
            if self.canal >= 0 and self.canal <= 200:
                self.canal = self.canal + 4
                print('-' * 45)
                print('                  CANAL {} '.format(self.canal))
                print('-' * 45)
            else:
                print('      CANAL {}, IMPOSSIVÉL IR PARA CIMA!'.format(self.canal))
                return
        else:
            print('-' * 45)
            print('PARA TROCAR DE CANAL A TV DEVE ESTAR LIGADA!')
            print('-' * 45)
    def diminuir_Canal(self):                                                 # DIMINUIR CANAL <<<<<<<<<<<<
        if self.ligada == True:
            if self.canal >= 4 and self.canal <= 196:
                self.canal = self.canal - 4
                print('-'*45)
                print('                  CANAL {}'.format(self.canal))
                print('-' * 45)
            elif self.canal <= 0:
                print('-'*45)
                print('      CANAL {}, IMPOSSIVÉL IR PARA BAIXO!'.format(self.canal))
                print('-' * 45)
        else:
            print('-'*45)
            print('PARA TROCAR DE CANAL A TV DEVE ESTAR LIGADA!')
            print('-'*45)
            return
    def tocar(self):                                                 # TOCANDO  <<<<<<
        if self.ligada == True:
            if self.tocando == False:
                print('-' * 45)
                print('              TOCANDO MÚSICA')
                print('-' * 45)
                self.tocando = True
            else:
                print('-'*45)
                print('            TOCANDO ESTÁ LIGADO')
                print('-' * 45)
        else:
            print('-' * 45)
            print('               TV DESLIGADA')
            print('-' * 45)
    def sair_Tocar(self):
        if self.ligada == True:
            if self.tocando == True:
                print('-'*45)
                print('                TOCANDO OFF')
                print('-' * 45)
                self.tocando = False
            else:
                print('                TOCANDO OFF')

        else:
            print('     TV DESLIGADA')
    def mudo(self):
        if self.ligada == True:
            if self.volume > 0:
                self.volume = 0
                print('-'*45)
                print('            M U D O')
                print('-' * 45)
            else:
                print('-' * 45)
                print('           VOLUME NO MUDO!')
                print('-' * 45)
        else:
            print('-' * 45)
            print('               TV DESLIGADA')
            print('-' * 45)
    def tirarMudo(self):
        if self.ligada == True:
            if self.volume == 0:
                self.volume = 50
                print('-' * 45)
                print('        VOLUME AUMENTADO PARA {}'.format(self.volume))
                print('-' * 45)
            elif self.volume > 0:
                print('-' * 45)
                print('        VOLUME NO {}, NÃO ESTÁ NO MUDO!'.format(self.volume))
                print('-' * 45)
            else:
                print('Impossivél colocar no MUDO')
        else:
            print('TV está desligada!')
    def escolher_canal(self):
        if self.ligada == True:
            var = int(input('DIGITE O CANAL: '))
            self.canal = var
            if self.canal >= 0 and self.canal <= 196:
                print('-'*45)
                print('          CANAL ESCOLHIDO: {}'.format(self.canal))
                print('-' * 45)
            else:
                print('-' * 45)
                print('          CANAL NÃO EXISTE')
                print('-' * 45)
        else:
            print('-' * 45)
            print('              TV DESLIGADA')
            print('-' * 45)
    def escolher_Volume(self):
        if self.ligada == True:
            vare = int(input('DIGITE O VOLUME: '))
            self.volume = vare
            if self.volume >= 0 and self.volume <= 200:
                print('-'*45)
                print('          VOLUME: {}'.format(self.volume))
                print('-' * 45)
            else:
                print('-' * 45)
                print('          VOLUME INSUFICIENTE')
                print('-' * 45)
        else:
            print('-'*45)
            print('              TV DESLIGADA!')
            print('-' * 45)
    def name(self):  # DISPLAY <<<<<<<<<<<<
        if self.ligada == True:
            print('-' * 45)
            print('               \033[34mD I S P L A Y\033[0m')
            print('-' * 45)

            if self.ligada == True:
                print('LIGADA: \033[0;32m{}\033[0m'.format(self.ligada))
            else:
                print('LIGADA: \033[1;31m{}\033[0m'.format(self.ligada))

            if self.ligada == True:
                print('CANAL: {}'.format(self.canal))
            elif self.ligada == False:
                self.canal = 0
                print('CANAL: {}'.format(self.canal))

            if self.ligada == True:
                print('VOLUME: {}'.format(self.volume))
            elif self.ligada == False:
                self.volume = 0
                print('VOLUME: {}'.format(self.volume))

            if self.ligada == True:
                if self.tocando == True:
                    print('TOCANDO: \033[0;32m{}\033[0m'.format(self.tocando))
                else:
                    print('TOCANDO: \033[1;31m{}\033[0m'.format(self.tocando))
            elif self.ligada == False:
                self.tocando = False
                print('TOCANDO: \033[0;31m{}\033[0m'.format(self.tocando))
        elif self.ligada == False:
            print('-'*45)
            print(' PARA \033[0;32mACESSAR\033[0m O DISPLAY, \033[0;32mLIGUE\033[0m A TV!')
            print('-'*45)





