print('\n --- Calc --- \n')

while True:
    cont = input('Deseja prosseguir ou sair? (1/2): ')

    if cont == '2':
        print('\n Até a próxima! \n')
        break

    elif cont == '1':
            n1 = float(input('\nDigite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            print()

            contas = ('1 - soma', '2 - Subtração', '3 - Divisão', '4 - Multiplicacão' )

            for n in contas:
                 print(n)
            print()
            
            conta = int(input('\nQual operação você deseja realizar? '))

            if conta == 1:
                print(f'\nO resultado é de {n1 + n2:.2f}\n')

            elif conta == 2:
                print(f'\nO resultado é de {n1 - n2:.2f}\n')

            elif conta == 3:
                if n2 == 0:
                    print('\nErro: Divisão por zero.\n')
                else:
                    print(f'\nO resultado é de {n1 / n2:.2f}\n')

            elif conta == 4:
                print(f'\nO resultado é de {n1 * n2:.2f}\n')
                
            else:
                print('\n Operação inválida.    \n')
    else:
         print('\n Caractere inválido. \n')
