import textwrap

def menu():
    menu="""\n
    -----Menu-----
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar conta
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n Deposito realizado.")
    else:
        print("\n Operação falhou. Valor inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = valor >= limite_saques

    if excedeu_saldo:
        print("\n Operação falhou. Saldo insuficiente.")

    elif excedeu_limite:
        print("\n Operação falhou. Excede o limite.")
    
    elif excedeu_saques:
        print("\n Operação falhou. Máximo de saques realizado")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado")
    else:
        print("Operacao falhou! O valor e invalido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("-----EXTRATO-----")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("-----------------")

def criar_usuario(usuarios):
    cpf = input("informe o cpf (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n CPF já cadastrado!")
        return
    
    nome = input("nome")
    data_nascimento = input("data (dd-mm-aaaa): ")
    endereco = input("endereco (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("usuario criado")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada!")
        return {"Agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuario nao encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif opcao == "s":
            valor = float(input("Informe o valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
    
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao =="lc":
            listar_contas(contas)

        elif opcao =="q":
            break

        else:
            print("Operacao invalida, selecione novamente!")

main()