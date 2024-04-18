menu =  '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''

saldo = 0;
limite = 500;
extrato = '''
'''
num_saques = 1;
LIMITE_SAQUES = 3;

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        print('Depósito')
        deposito = float(input('Digite o valor do depósito: '))
        if deposito >0:
            saldo += deposito
            print(f'R${deposito} foi adicionado à conta.')
            extrato += f'Foi adicionado R${deposito} à conta. \n'
        
        else: print("Valor Inválido.")
        
    
    elif opcao == 's':
        print('Saque')
        if num_saques <= LIMITE_SAQUES:
            saque = float(input('Digite um valor pra saque: '))
            if saque <= saldo and saque <= limite and saque >0:
                saldo -= saque
                print(f'R${saque} foi sacado com sucesso.')
                extrato += f'Foi realizado um saque de R${saque} na conta. \n'
                num_saques +=1

            else:
                print('Valor inválido ou saldo indisponível.')
                
        else:
         print('Você atingiu o limite de saque.')
    
        
    
    elif opcao == 'e':
        print("Extrato: ")
        print(f'O Saldo atual é R${saldo} \n')
        print(extrato)
        
    
    elif opcao == 'q':
        print('Você escolheu sair do sistema.')
        break

    else:
        print('Operação Inválida. Por favor, selecione novamente a função desejada')
