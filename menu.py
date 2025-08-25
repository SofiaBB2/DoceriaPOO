from models import TipoDoce, Doce


def cadastrarTipo():
    op = 1
    while(op != 0):
        # Usuário informa o valor de cada atributo.
        print("Cadastre um tipo de doce: ")
        classificacao = input("Informe a classificação do doce: ")
        sabor = input("Informe o sabor: ")
        tipoPreco = None
        while(tipoPreco == None):
            tipoPreco = input("O doce será pago por peso Kg ou por unidade? (Responder (Kg) ou (unidade)). ")
            if (tipoPreco.casefold() == "unidade".casefold()):
                tipoPreco = True
            elif(tipoPreco.casefold() == "Kg".casefold()):
                tipoPreco = False
            else:
                print("Erro! Valor inválido.")
        preco = float(input("Informe o preço do doce: "))
        disponivel = input("O doce está disponível? ")
        if (disponivel.casefold() == "sim".casefold()):
            disponivel = True
        else:
            disponivel = False

        # Cadastra o objeto no BD.
        tipoCad = TipoDoce.create(classificacao=classificacao, sabor=sabor, tipoPreco=tipoPreco, preco=preco, disponivel=disponivel)
        # Verifica se o usuário quer cadastrar mais tipos de doces.
        op = int(input("Deseja cadastrar outro tipo de doce (0 ou 1)? "))
    
    print("Cadastro concluído!")

def editarTipo():
    
    # Mostra os Tipos de Doces cadastrados para que usuário saiba escolher o ID correto.
    mostrarTipos()
    
    # Usuário informa o ID a ser atualizado.
    idAt = int(input("Qual é o ID do tipo de doce que deseja atualizar? "))
    tipoAt = TipoDoce.get(TipoDoce.id == idAt)
    print(tipoAt)
    # Usuário informa qual atributo deseja atualizar e qual é o novo valor.
    op = -1
    while(op != 0):
        print("0 - sair;")
        print("1 - classificação;")
        print("2 - sabor;")
        print("3 - tipoPreço;")
        print("4 - preco;")
        print("5 - disponivel.")
        op = int(input("O que deseja alterar? "))

        if(op == 0):
            break
        elif (op == 1):
            tipoAt.classificacao = input("Informe a classificação do doce: ")
            tipoAt.save()
        elif(op == 2):
            tipoAt.sabor = input("Informe o sabor: ")
            tipoAt.save()
        elif(op == 3):
            tipoAt.tipoPreco = bool(input("O doce será pago por peso em Kg(False) ou por unidade(True)? "))
            tipoAt.save()
        elif(op == 4):
            tipoAt.preco = float(input("Informe o preço do doce: "))
            tipoAt.save()
        elif(op == 5):
            tipoAt.disponivel = bool(input("Informe se o doce está disponível(True) ou não(False): "))
            tipoAt.save()
        else:
            print("Opção inválida!")
     
    print("Atualização concluída!")

def mostrarTipos():
    print("\n--------------------Tipos de Doces Cadastrados---------------------\n")
    
    # Seleciona a lista de tipos de doces.
    tiposCad = TipoDoce.select()
    # Mostra todos os atributos de cada tipo de doce.
    for doce in tiposCad:
        print(f"Classificação: {doce.classificacao} (ID: {doce.id})")
        print(f"Sabor: {doce.sabor}")
        if doce.tipoPreco:
            print(f"O preço do doce por unidade é R${doce.preco}")
        else:
            print(f"O preço do doce por kg é R${doce.preco}")
        if doce.disponivel:
            print(f"O doce está disponível.")
        else: 
            print(f"O doce não está disponível.")
        print("\n---------------------------------------------------------\n")

def excluirTipo():
    # Mostra os Tipos de Doces cadastrados para que usuário saiba escolher o ID correto.
    mostrarTipos()
    # Usuário informa qual atributo deseja excluir.
    idExcluir = int(input("\nQual é o ID do tipo de doce que deseja excluir? "))
    # Seleciona o tipo de doce do ID informado pelo usuário e exclui do BD.
    tipoEx = TipoDoce.get(TipoDoce.id == idExcluir)
    tipoEx.delete_instance()
    print(f"Tipo de Doce removido do banco de dados")

def cadastrarDoce():
    op = 1
    while(op != 0):
        # Usuário informa o valor de cada atributo.
        print("Cadastre um doce vendido: ")
    
        peso = float(input("Informe o peso do doce: "))
        # Mostra os Tipos de Doces cadastrados para que usuário saiba escolher o ID correto.
        mostrarTipos()
        idTipo = int(input("Informe o ID do tipo de doce que pertence: "))

        # Cadastra o objeto no BD
        doceCad = Doce.create(peso=peso, tipo=idTipo)
        # Verifica se o usuário quer cadastrar mais doces vendidos.
        op = int(input("Deseja cadastrar outro doce vendido (0 ou 1)? "))
    
    print("Cadastro concluído!")

def mostrarDoces():
    print("\n-----------------Doces Vendidos----------------------\n")
    # Seleciona a lista de doces.
    doces = Doce.select()
    # Mostra todos os atributos de cada doce.
    for doce in doces:
        print(f"(ID: {doce.id})")
        print(f"Peso: {doce.peso}g")
        # Tenta mostrar os atributos do Tipo de Doce relacionado àquele doce.
        try:
            print(f"Tipo de Doce: {doce.tipo.classificacao}")
            print(f"Sabor: {doce.tipo.sabor}")
            if doce.tipo.tipoPreco:
                print(f"O preço do doce por unidade é R${doce.tipo.preco}")
            else:
                print(f"O preço do doce por kg é R${doce.tipo.preco}")
            if doce.tipo.disponivel:
                print(f"O doce está disponível.")
            else: 
                print(f"O doce não está disponível.")
            print("\n---------------------------------------------------------\n")
        # Caso não encontre aquele ID de Tipo de Doce, avisa que foi exluído.
        except:
            print("O Tipo desse Doce foi excluído!")
            print("\n---------------------------------------------------------\n")

def excluirDoce():
    # Mostra os Doces cadastrados para que usuário saiba esccolher o ID correto.
    mostrarDoces()

    # Usuário informa o ID a ser excluído.
    idExcluir = int(input("\nQual é o ID do doce que deseja excluir? "))
    # Seleciona o doce do ID informado pelo usuário e exclui do BD.
    doceEx = Doce.get(Doce.id == idExcluir)
    doceEx.delete_instance()
    print(f"Doce removido do banco de dados.")

def editarDoce():
    # Mostra os Doces cadastrados para que usuário saiba esccolher o ID correto.
    mostrarDoces()

    # Usuário informa o ID a ser atualizado.
    idAt = int(input("Informe o ID do doce que deseja alterar: "))
    doceAt = Doce.get(Doce.id == idAt)

    # Usuário informa qual atributo deseja atualizar e qual é o novo valor.
    op = -1
    while(op != 0):
        print("0 - sair;")
        print("1 - peso;")
        print("2 - tipo;")
        op = int(input("O que deseja alterar? "))

        if(op == 0):
            break
        elif(op == 1):
            doceAt.peso = input("Informe o novo peso do doce: ")
            doceAt.save()
        elif(op == 2):
            mostrarTipos()
            idTipo = int(input("Informe o ID do tipo de doce que pertence: "))
            doceAt.save
        else:
            print("Opção inválida!")
     
    print("Atualização concluída!")

def menuOps2(op):
    op2 = -1
    # Exibe o Menu de Operações enquanto o usuário quiser continuar.
    while(op2 != 0):
        print("\n-----------------MENU DE OPERAÇÕES------------------\n")
        print("0 - cancelar;")
        print("1 - cadastrar;")
        print("2 - mostrar;")
        print("3 - excluir;")
        print("4 - editar.")
        op2 = int(input("\nQual é a opção escolhida? " ))

        if(op == 1):
            if(op2 == 1):
                cadastrarTipo()
            elif(op2 == 2):
                mostrarTipos()
            elif(op2 == 3):
                excluirTipo()
            elif(op2 == 4):
                editarTipo()
            else:
                print("Opção inválida!")
        else:
            if(op2 == 1):
                cadastrarDoce()
            elif(op2 == 2):
                mostrarDoces()
            elif(op2 == 3):
                excluirDoce()
            elif(op2 == 4):
                editarDoce()
            else:
                print("Opção inválida!")


def menuOps():
    op = -1
    print("Seja bem-vindo(a) à Doceria da Alegria!")

    # Exibe o Menu Geral enquanto o usuário quiser continuar.
    while(op != 0):
        print("\n-----------------MENU GERAL------------------\n")
        print("0 - sair do programa;")
        print("1 - Tipos de Doces;")
        print("2 - Doces Vendidos.")
        op = int(input("\nQual é a opção escolhida?\n" ))

        if(op == 0):
            print("Fim!")
            break
        elif(op == 1 or op == 2):
            menuOps2(op)
        else:
            print("Opção inválida!")
            

menuOps()
