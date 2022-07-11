from classes.fornecedor import Fornecedor
from classes.cliente import Cliente
from classes.produtos import Produtos
from classes.adquirir import Adquirir
from classes.fornecer import Fornecer

resp = -1

while resp != 0:

    print("Digite qual opção você quer fazer alterações:")
    print("Digite [ 1 ] para acessar Fornecer ")
    print("Digite [ 2 ] para acessar Adquirir ")
    print("Digite [ 3 ] para acessar Produtos ")
    print("Digite [ 4 ] para acessar Cliente ")
    print("Digite [ 5 ] para acessar Fornecedor ")
    print("Digite [ 0 ] para SAIR ")

    resp = int(input('Opcao escolhida: '))
    print('')

    if resp == 1:

        x = Fornecer()
        resp2 = -1

        while resp2 != 0:

            print("\nDigite qual opção você deseja:")
            print("Digite [ 1 ] para acessar getFornecer ")
            print("Digite [ 2 ] para acessar setFornecer ")
            print("Digite [ 3 ] para acessar deleteFornecer ")
            print("Digite [ 0 ] para SAIR ")

            resp2 = int(input('Opcao escolhida: '))
            
            if resp2 == 1:
                
                print(x.getFornecer())

            elif resp2 == 2:

                a = input('Digite a data: ')
                b = int(input('Digite o ID do produto: '))
                c = int(input('Digite o Codigo do fornecedor: '))

                x.setFornecer(a, b, c)

            elif resp2 == 3:

                a = input('Digite a data: ')
                b = int(input('Digite o ID do produto: '))
                c = int(input('Digite o Codigo do fornecedor: '))

                x.deleteFornecer(a, b, c)

            elif resp2 == 0:

                print('Saindo...\n')

            else:
                print('Opcao Invalida! Tente novamente')

    elif resp == 2:
        x = Adquirir()
        resp2 = -1
        
        while resp2 != 0:

            print("\nDigite qual opção você deseja:")
            print("Digite [ 1 ] para acessar getAdquirir ")
            print("Digite [ 2 ] para acessar setAdquirir ")
            print("Digite [ 3 ] para acessar deleteAdquirir ")
            print("Digite [ 0 ] para SAIR ")

            resp2 = int(input('Opcao escolhida: '))
            print('')

            if resp2 == 1:

                print(x.getAdquirir())

            elif resp2 == 2:

                a = input('Digite a data: ')
                b = int(input('Digite o ID do produto: '))
                c = int(input('Digite o CPF do cliente: '))

                x.setAdquirir(a, b, c)

            elif resp2 == 3:

                a = input('Digite a data: ')
                b = int(input('Digite o ID do produto: '))
                c = int(input('Digite o CPF do cliente: '))

                x.deleteAdquirir(a, b, c)
            
            elif resp2 == 0:

                print('Saindo...\n')

            else:
                print('Opcao Invalida! Tente novamente')

    elif resp == 3:
        x = Produtos()
        resp2 = -1
        
        while resp2 != 0:

            print("\nDigite qual opção você deseja:")
            print("Digite [ 1 ] para acessar getProduto ")
            print("Digite [ 2 ] para acessar getProdutoByName ")
            print("Digite [ 3 ] para acessar setProduto ")
            print("Digite [ 4 ] para acessar updateProduto ")
            print("Digite [ 5 ] para acessar deleteProduto ")
            print("Digite [ 0 ] para SAIR ")

            resp2 = int(input('Opcao escolhida: '))
            print('')

            if resp2 == 1:

                print(x.getProduto())

            elif resp2 == 2:

                a = input('Digite o nome: ')

                print(x.getProdutoByName(a))

            elif resp2 == 3:

                a = input('Digite o nome: ')
                b = float(input('Digite o valor: '))
                c = input('Digite o tipo: ')

                x.setProduto(a, b, c)

            elif resp2 == 4:

                a = input('Digite o nome: ')
                b = float(input('Digite o valor: '))

                x.updateProduto(a, b)

            elif resp2 == 5:

                a = int(input('Digite o ID: '))

                x.deleteProduto(a)
            
            elif resp2 == 0:

                print('Saindo...\n')
                
            else:
                print('Opcao Invalida! Tente novamente')
            
    elif resp == 4:
        x = Cliente()
        resp2 = -1
        
        while resp2 != 0:

            print("\nDigite qual opção você deseja:")
            print("Digite [ 1 ] para acessar getCliente ")
            print("Digite [ 2 ] para acessar getClienteByCpf ")
            print("Digite [ 3 ] para acessar setCliente ")
            print("Digite [ 4 ] para acessar updateCliente ")
            print("Digite [ 5 ] para acessar deleteCliente ")
            print("Digite [ 0 ] para SAIR ")

            resp2 = int(input('Opcao escolhida: '))
            print('')

            if resp2 == 1:

                print(x.getCliente())

            elif resp2 == 2:

                a = int(input('Qual o CPF? '))
                print(x.getClienteByCpf(a))

            elif resp2 == 3:

                a = input('Digite o nome: ')
                b = int(input('Digite o CPF: '))
                c = input('Digite o telefone: ')
                d = input('Digite o endereco: ')

                x.setCliente(a, b, c, d)

            elif resp2 == 4:

                a = int(input('Qual o CPF? '))
                b = input('Digite o NOVO endereco: ')
                c = input('Digite o NOVO numero de telefone: ')

                x.updateCliente(a, c, b)

            elif resp2 == 5:

                a = int(input('Qual o CPF? '))

                x.deleteCliente(a)
            
            elif resp2 == 0:

                print('Saindo...\n')
                
            else:
                print('Opcao Invalida! Tente novamente')
            
    elif resp == 5:
        x = Fornecedor()
        resp2 = -1
        
        while resp2 != 0:

            print("\nDigite qual opção você deseja:")
            print("Digite [ 1 ] para acessar getFornecedor ")
            print("Digite [ 2 ] para acessar setFornecedor ")
            print("Digite [ 3 ] para acessar updateFornecedor ")
            print("Digite [ 4 ] para acessar deleteFornecedor ")
            print("Digite [ 0 ] para SAIR ")

            resp2 = int(input('Opcao escolhida: '))
            print('')
            
            if resp2 == 1:

                print(x.getFornecedor())

            elif resp2 == 2:

                a = input('Digite o nome: ')
                b = input('Digite o telefone: ')
                c = input('Digite o endereco: ')

                x.setFornecedor(a, b, c)

            elif resp2 == 3:

                a = input('Digite o nome: ')
                b = input('Digite o telefone: ')
                c = input('Digite o endereco: ')

                x.updateFornecedor(a, b, c)

            elif resp2 == 4:

                a = input('Digite o nome: ')

                x.deleteFornecedor(a)
            
            elif resp2 == 0:

                print('Saindo...\n')
                
            else:
                print('Opcao Invalida! Tente novamente')