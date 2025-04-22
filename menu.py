from models import TipoDoce

def menuOps():
    print("Seja bem-vindo(a) à Doceria da Alegria! O que você gostaria de fazer?")
    print("1 - cadastrar novos tipos de doce;")
    print("2 - mostrar todos os tipos de doces;")
    print("3 - cadastrar um doce vendido;")
    print("4 - editar tipos de doces;")
    print("...")

    op = int(input("Qual é a opção escolhida?" ))
    if(op == 1):
        cadastrarTipo()
    elif(op == 2):
        mostrarTipos()
    else:
        print("Opção não encontrada!")

def cadastrarTipo():
    # Usuário informa o valor de cada atributo.
    print("Cadastre um tipo de doce: ")
    classificacao = input("Informe a classificação do doce: ")
    sabor = input("Informe o sabor: ")
    tipoPreco = bool(input("O doce será pago por peso em Kg(False) ou por unidade(True)? "))
    preco = float(input("Informe o preço do doce: "))
    disponivel = bool(input("Informe se o doce está disponível(True) ou não(False): "))

    # Cadastra o objeto no BD
    tipoCad = TipoDoce.create(classificacao=classificacao, sabor=sabor, tipoPreco=tipoPreco, preco=preco, disponivel=disponivel)


def mostrarTipos():
    print("--------------------Doces Cadastrados---------------------")

    tiposCad = TipoDoce.select()
    for doce in tiposCad:
        print("\n --------------------------------------------------------- \n")
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

menuOps()