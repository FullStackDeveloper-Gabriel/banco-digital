print("Banco Central")
print(" ")

# FUNÇÃO --> DADOS PESSOAIS
username = input("Inserir Nome de Usuário: ")
cpf = input("Inserir CPF: ")
birthday = input("Inserir Data de Nascimento: ")
print(f'''
----------------------------------------------------
                    SAUDAÇÕES
    Seja bem vindo {username} ao Banco Central!
----------------------------------------------------
                    SEUS DADOS
    CPF: {cpf}
    Data de Nascimento: {birthday}
    ''')

# FUNÇÃO --> SACAR
def saque(saldo, funcao_sacar, valor_saque):
    valor_saque = float(input("Insira o valor do saque: "))
    if valor_saque > saldo:
      print("Saldo Insuficiente")
    else:
      funcao_sacar = saldo - valor_saque
      print(f'''
      Saque realizado com sucesso!
      Saldo atual: R${funcao_sacar}
      ''')

# FUNÇÃO --> DEPOSITAR
def deposito(saldo, funcao_depositar, valor_deposito):
    valor_deposito = float(input("Insira a quantia do depósito: "))
    funcao_depositar = saldo + valor_deposito
    print(f'''
      Depósito realizado com sucesso!
      Saldo atual: R${funcao_depositar}
      ''')

def direcionar():
    print(" ")

def banco():
    saldo = 1000
    print(f'''
                    SALDO
    Saldo atual: R${saldo}
----------------------------------------------------
                    OPÇÕES DE SERVIÇOS
    (1) - SAQUE
    (2) - DEPÓSITO
    (3) - SAIR
    ''')
    escolha_opcao = input("Escolha uma das opções acima: ")
    direcionar()

    if escolha_opcao == "1":
        valor_saque = float(input("Insira o valor do saque: "))
        if valor_saque > saldo:
          print("Saldo Insuficiente")
        else:
          funcao_sacar = saldo - valor_saque
          print(f'''
          Saque realizado com sucesso!
          Saldo atual: R${funcao_sacar}
          ''')
    elif escolha_opcao == "2":
         valor_deposito = float(input("Insira a quantia do depósito: "))
         funcao_depositar = saldo + valor_deposito
         print(f'''
          Depósito realizado com sucesso!
          Saldo atual: R${funcao_depositar}
          ''')
    elif escolha_opcao == "3":
         r = sair_do_sistema(sair)
         print(r)
    else:
         print("Opção invalida. Tente novamente!")

while True:
  banco()
