class Console:
    args = []
    def ex_Produt(self):
        print('   ------ EXCLUIR CÓDIGO DE BARRAS -----')
        print('Codigos cadastrados: {}'.format(con.args))
        if len(con.args) > 0:
            for i in range(len(con.args)):
                name = int(input('DIGITE O CÓDIGO A SER EXCLUIDO: '))
                if name in con.args:
                    print('Removendo...')
                    con.args.remove(name)
                    print('Código {} removido com sucesso.'.format(name))
                    break
                else:
                    print()
                    print('Código Inválido.')
                    print()
                    return con.ex_Produt()
        elif len(con.args) <= 0:
            print('Ainda não há códigos cadastrados.')
            zhut = str(input('Quer cadastrar um produto? [S/N]')).upper()
            if zhut == 'S':
                con.cad_Produt()
            elif zhut == 'N':
                return
            else:
                print('Comando inválido.')
                return
    def cad_Produt(self):
        numcod = int(input('Digite quantos códigos quer cadastrar: '))
        for i in range(0, numcod):
            cod = int(input('DIGITE O CÓDIGO DE BARRAS DO PRODUTO: '))
            if cod in con.args:
                print('Código já foi cadastrado')
                return con.cad_Produt()
            else:
                con.args.append(cod)
                for x in range(len(con.args)):
                    print('Codigo {} armazenado na posição {} '.format(cod, x))
            con.codel()
        print('-'*50)
        print('TOTAL DE CÓDIGOS CADASTRADOS: {}'.format(len(con.args)))
        con.sair()
    def sair(self):
        print('-' * 50)
        choice = input('QUER CONTINUAR CADASTRANDO: [S/N] ').upper()
        if choice == 'S':
            return con.cad_Produt()
        elif choice == 'N':
            print('-'*50)
            print('                    SAINDO')
            print('-' * 50)
            return
    def codel(self):
        print('-'*50)
        print(' L I S T A   C Ó D I G O S   C A D A S T R A D O S')
        print('-'*50)
        print('TOTAL DE CÓDIGOS DE PRODUTOS CADASTRADOS: {} '.format(len(con.args)))
        for x in range(len(con.args)):
            print(con.args[x], 'na posição', x+1)
con = Console()

