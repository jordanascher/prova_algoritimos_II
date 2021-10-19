from Furadeira import Furadeira
from Lixadeira import Lixadeira

# menu = True
opcao = 1

arrFuradeira = []
arrLixadeira = []

while opcao > 0:
    print("""
        ============== MENU ==================
        1 - Cadastro Furadeira
        2 - Cadastro Lixadeira
        3 - Relatório Furadeira
        4 - Relatório Lixadeira
        0 - Sair
    """)
    opcao = int(input("Informe a opção desejada: "))
    
    if opcao == 1:
        
        # recebe os valores do usuário
        nome = input("Informe o nome: ")
        tensao = input("Informe a tensao: ")
        preco = input("Informe o preço: ")
        potencia = input("Informe a potência: ")

        # instancia novo objeto - Furadeira
        furadeira = Furadeira()
        furadeira.cadastrar(nome, tensao, preco, potencia)
        arrFuradeira.append(furadeira)
        
    elif opcao == 2:
        
        # recebe os valores do usuário
        nome = input("Informe o nome: ")
        tensao = input("Informe a tensao: ")
        preco = input("Informe o preço: ")
        
        # Validação - Valor numérico
        valid = False
        while valid == False: 
            rotacoes = input("Informe as rotações: ")

            if rotacoes.isnumeric() == True:
                valid = True
            else:
                print("Informe um valor numérico")
        
        # instancia novo objeto - Lixadeira
        lixadeira = Lixadeira()
        lixadeira.cadastrar(nome, tensao, preco, int(rotacoes))
        arrLixadeira.append(lixadeira)
        
    elif opcao == 3:
        # Relatório Furadeira
        print("\n==== RELATÓRIO - " + str(len(arrFuradeira)) + " Furadeira(s) ====")
        
        if len(arrFuradeira) == 0:
            print("Nenhuma furadeira cadastrada")

        else:
            for furadeira in arrFuradeira:
                print(furadeira.getInformacoes())
        
    elif opcao == 4:
        # Relatório Furadeira
        print("\n==== RELATÓRIO - "+ str(len(arrLixadeira)) + " Lixadeiras ====")
        for lixadeira in arrLixadeira:
            print(lixadeira.getInformacoes())

    elif opcao == 0:
        print("Saindo...")
    else:
        print("Informe uma opção correta")

