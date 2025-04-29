from models import TipoDoce, Doce


def cadastrarTipo():
    op = True
    while(op):
        # Usuário informa o valor de cada atributo.
        print("Cadastre um tipo de doce: ")
        classificacao = input("Informe a classificação do doce: ")
        sabor = input("Informe o sabor: ")
        tipoPreco = bool(input("O doce será pago por peso em Kg(False) ou por unidade(True)? "))
        preco = float(input("Informe o preço do doce: "))
        disponivel = bool(input("Informe se o doce está disponível(True) ou não(False): "))

        # Cadastra o objeto no BD
        tipoCad = TipoDoce.create(classificacao=classificacao, sabor=sabor, tipoPreco=tipoPreco, preco=preco, disponivel=disponivel)
        op = bool(input("Deseja cadastrar outro tipo de doce?\n"))
    
    print("Cadastro concluído!")

def mostrarTipos():
    print("\n--------------------Tipos de Doces Cadastrados---------------------\n")

    tiposCad = TipoDoce.select()
    for doce in tiposCad:
        print(f"Classificação: {doce.classificacao}")
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
    
def mostrarDoces():
    print("\n-----------------Doces Vendidos----------------------\n")
    doces = Doce.select()

    for doce in doces:
        print(f"Peso: {doce.peso}")
        print(f"Tipo de Doce: {doce.tipo.classificacao}")
        print(f"Sabor: {doce.tipo.sabor}")
        if doce.tipoPreco:
            print(f"O preço do doce por unidade é R${doce.tipo.preco}")
        else:
            print(f"O preço do doce por kg é R${doce.tipo.preco}")
        if doce.tipo.disponivel:
            print(f"O doce está disponível.")
        else: 
            print(f"O doce não está disponível.")
        print("\n---------------------------------------------------------\n")

def menuOps2(op):
    while(op2 != 0):
        print("\n-----------------MENU DE OPERAÇÕES------------------\n")
        print("0 - cancelar;")
        print("1 - cadastrar;")
        print("2 - mostrar;")
        print("3 - excluir;")
        print("4 - editar.")
        op2 = int(input("\nQual é a opção escolhida?\n" ))

        if(op == 1):
            if(op2 == 1):
                cadastrarTipo()
            elif(op2 == 2):
                mostrarTipos()
            elif(op2 == 3):
                print("Incluir 'excluirTipo()'")
                #excluirTipo()
            elif(op2 == 4):
                print("Incluir 'editarTipo()'")
                #editarTipo()
            else:
                print("Opção inválida!")
        else:
            if(op2 == 1):
                print("Incluir cadastrarDoce()")
                #cadastrarDoce()
            elif(op2 == 2):
                mostrarDoces()
            elif(op2 == 4):
                print("Incluir editarDoce()")
                #editarDoce()
            else:
                print("Opção inválida!")


def menuOps():
    op = -1
    print("Seja bem-vindo(a) à Doceria da Alegria!")

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
