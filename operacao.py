menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

extrato_dict = {}
operacao_list = []
valor_list = []
saldo = 0
LIMITE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    # depósito
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor

            # registro da operação
            operacao_list.append('Depósito')
            valor_list.append(f'R$ {valor:.2f}')
            extrato_dict['operacao'] = operacao_list
            extrato_dict['valor'] = valor_list

        else:
            print('Falha de operação! O valor informado é invalido')

    # saque
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        # regras
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Falha de operação! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Falha de operação! O valor do saque excedeu o limite.')

        elif excedeu_saques:
            print('Falha de operação! Número máximo de saques excedido.')

        elif valor > 0:
            saldo -= valor

            # registro da operação
            operacao_list.append('Saque')
            valor_list.append(f'R$ {valor:.2f}')
            extrato_dict['operacao'] = operacao_list
            extrato_dict['valor'] = valor_list

            numero_saques += 1

        else:
            print('Falha de operação! O valor informado é inválido.')

    # extrato
    elif opcao == 'e':
        print('\n================= EXTRATO =================')
        if extrato_dict == {}:
            print('Não foram realizadas movimentações.')
            print(f'\nSaldo: R$ {saldo:.2f}')
            print('===========================================')

        else:

            for op, val in zip(extrato_dict['operacao'], extrato_dict['valor']):
                print(f'{op}: {val}')

            print(f'\nSaldo: R$ {saldo:.2f}')  
            print('===========================================')

    # encerramento
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
