import os, time


def menu():
   
    menu = """
      \n 𝑴𝑬𝑵𝑼\n
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
      
        [nu] Novo usuário
        [q] Sair
    """
    return input(menu).lower()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        
        extrato += f"Depósito no valor de {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("A operação falhou! O valor informado é inválido.")
        
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    exedeu_saldo = valor > saldo
    exedeu_limite = valor > limite
    exedeu_saques = numero_saques > limite_saques
    
    if exedeu_saldo:
        print("A operação falhou! Saldo insuficiente.")
    
    elif exedeu_limite:
        print("A operação falhou! Limite de saque até R$ 500,00")
        
    elif exedeu_saques:
        print("A operação falhou! Você exedeu o limite de saque diário")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque no valor de R$ {valor:.2f}\n"
        print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
        numero_saques += 1
        print("saques: ",numero_saques)
    
    else:
        print("ERRO! VAlor inválido.")

    return saldo, extrato
        
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def extrato():
    pass

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuarios:
        print("Usuário já cadastrado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa)")
    endereco = input("Informen o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nacsc": data_nascimento, "endereco": endereco})
    
    print("Usuário cadastrado com sucesso!")
    

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuarios:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado")

def main():
    LIMITE_SAQUE = 3
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
            valor = float(input("\nInforme o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
            time.sleep(3)
            os.system("cls")
        
        
        elif opcao == "s":
             valor = float(input("\nInforme o valor do saque: "))
             
             saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUE)
             time.sleep(3)
             os.system("cls")
             
        elif opcao == "nu":
            criar_usuario(usuarios)
            time.sleep(3)
            os.system("cls")
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)


        elif opcao == "q":
            break
        
        else:
            print("Opção inválida")
main()