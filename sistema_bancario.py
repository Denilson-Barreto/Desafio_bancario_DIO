menu = """
        MENU
    
    [d]  -  Deposito
    [s]  -  Sacar
    [e]  -  Extrato
    [q]  -  Sair
"""

saldo = 0
limiti = 500
numero_saque = 0
LIMITE_SAQUE = 3
extrato = ""

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor de deposito:  "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"   Deposito: R$ {valor_deposito:.2f}    \n"
        else:
            print("Valor invalido para deposito, tente novamente.")

    elif opcao == "s":

        if numero_saque < LIMITE_SAQUE:
            valor_saque = float(input("Informe o valor do saque desejado:   "))

            if valor_saque <= saldo and valor_saque <= limiti:
                saldo -= valor_saque
                extrato += f"   Saque: R$ {valor_saque:.2f}  \n"
                numero_saque += 1
            elif valor_saque > limiti:
                print("Valor de saque acima do limite permitido.")
            else:
                print("Valor de saque invalido, saldo insuficiente.")
                
        else:
            print("valor de saques diarios atingido.")

    elif opcao == "e":
        print("\n________________________________________")
        print("\n                extrato                 ")
        print("\n   Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\n  SALDO: R$ {saldo:.2f}    ")
        print("\n________________________________________")

    elif opcao == "q":
        break

    else:
        print("Escolha uma das opções do MENU:  ")