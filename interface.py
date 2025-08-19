import tkinter as tk
from models import TipoDoce
from tkinter import messagebox as mb


def limpar_tela():
    for widget in janela.winfo_children():
        widget.grid_remove()

def restaurar_tela():
    for widget in janela.winfo_children():
        widget.grid()

def limparCampos():
    classificacaoEt.delete(0, tk.END)
    saborEt.delete(0, tk.END)
    tipoPrecoEt.delete(0, tk.END)
    precoEt.delete(0, tk.END)
    disponivelEt.delete(0, tk.END)

def cadastrarTipo():
    classificacao = classificacaoEt.get()

    sabor = saborEt.get()

    tipoPreco = tipoPrecoEt.get()
    if (tipoPreco.casefold() == "unidade".casefold()):
        tipoPreco = True
    elif(tipoPreco.casefold() == "Kg".casefold()):
        tipoPreco = False
    else:
        mb.showerror("Erro em Tipo de Preço", "Informe um valor válido! ('Kg' ou 'unidade')")

    try:
        preco = float(precoEt.get())
    except:
        mb.showerror("Erro em Preço", "Informe um valor válido! (algum valor numérico)")

    disponivel = disponivelEt.get()
    if (disponivel.casefold() == "sim".casefold()):
        disponivel = True
    else:
        disponivel = False

    # Cadastra o objeto no BD.
    tipoCad = TipoDoce.create(classificacao=classificacao, sabor=sabor, tipoPreco=tipoPreco, preco=preco, disponivel=disponivel)

    limparCampos()

    mb.showinfo("Cadastro concluído", "Cadastrado com sucesso!")

def pegarSelecao():
    selecao = tiposDeDocesCad.curselection()
    if selecao: 
        indice = selecao[0]
        texto = tiposDeDocesCad.get(indice)
        print(f"Selecionado: {texto}, Indice: {indice}")
        return indice
    else:
        print("Nenhum item selecionado")
        return -1

def editarTipo():
    indice = pegarSelecao()
    if indice == -1:
        return

    if (((indice-1) % 6) == 0):
        idAt = indice-1
        print(f"idAt: {idAt}")

    elif(((indice-2) % 6 ) == 0):
        idAt = indice-2
        print(f"idAt: {idAt}")
        
    elif(((indice-3) % 6 ) == 0):
        idAt = indice-3
        print(f"idAt: {idAt}")
        
    elif(((indice-4) % 6 ) == 0):
        idAt = indice-4
        print(f"idAt: {idAt}")
        
    else:
        mb.showerror("Opção inválida", "Item selecionado não pode ser alterado.")
    
    tipoAt = TipoDoce.get(TipoDoce.id == idAt)
    
    limpar_tela()

    # Campos globais para acesso em 'salvar'
    global classificacaoEt, saborEt, tipoPrecoEt, precoEt, disponivelEt

    def salvar():
        if (((indice-1) % 6) == 0):
            tipoAt.classificacao = classificacaoEt.get()
        
        elif (((indice-2) % 6) == 0):
            tipoAt.sabor = saborEt.get()

        elif (((indice-3) % 6) == 0):
            tipoPreco = tipoPrecoEt.get()
            preco = precoEt.get()

            if tipoPreco.lower() == "unidade":
                tipoAt.tipoPreco = True
            elif tipoPreco.lower() == "kg":
                tipoAt.tipoPreco = False
            else:
                mb.showerror("Erro", "Tipo de preço inválido!")
                return

            try:
                tipoAt.preco = float(preco)
            except ValueError:
                mb.showerror("Erro", "Preço inválido!")
                return

        elif (((indice-4) % 6) == 0):
            disponivel = disponivelEt.get()
            tipoAt.disponivel = disponivel.lower() == "sim"

        tipoAt.save()
        mb.showinfo("Sucesso", "Atualizado com sucesso!")
        limpar_tela()
        restaurar_tela()

    # Criação dos campos com base na seleção
    if (((indice-1) % 6) == 0):
        classificacaoLb = tk.Label(text="Classificação:")
        classificacaoLb.grid(column=0, row=1)
        classificacaoEt = tk.Entry()
        classificacaoEt.grid(column=1, row=1)

    elif (((indice-2) % 6) == 0):
        saborLb = tk.Label(text="Sabor:")
        saborLb.grid(column=0, row=2)
        saborEt = tk.Entry()
        saborEt.grid(column=1, row=2)

    elif (((indice-3) % 6) == 0):
        tipoPrecoLb = tk.Label(text="Tipo de Preço (Kg/unidade):")
        tipoPrecoLb.grid(column=0, row=3)
        tipoPrecoEt = tk.Entry()
        tipoPrecoEt.grid(column=1, row=3)

        precoLb = tk.Label(text="Preço:")
        precoLb.grid(column=0, row=4)
        precoEt = tk.Entry()
        precoEt.grid(column=1, row=4)

    elif (((indice-4) % 6) == 0):
        disponivelLb = tk.Label(text="Está disponível? (Sim/Não):")
        disponivelLb.grid(column=0, row=5)
        disponivelEt = tk.Entry()
        disponivelEt.grid(column=1, row=5)

    else:
        mb.showerror("Erro", "Item não pode ser editado")
        return

    # Botões
    limparBt = tk.Button(text="Limpar", command=limparCampos)
    limparBt.grid(column=1, row=6)

    salvarBt = tk.Button(text="Salvar", command=salvar)
    salvarBt.grid(column=2, row=6)
    
janela = tk.Tk("Doceria POO")
janela.geometry("700x700")

tituloLb = tk.Label(text="Cadastrar Tipo de Doce", font=("Times New Roman", 16,"bold"), justify="center")
tituloLb.grid(padx=5, pady=7, column=0, row=0, columnspan=3)


classificacaoLb = tk.Label(text="Classificação:", font=("Times New Roman", 14))
classificacaoLb.grid(padx=5, pady=7, column=0, row=1, sticky="w")
classificacaoEt = tk.Entry()
classificacaoEt.grid(padx=5, pady=7, column=1, row=1, columnspan=2, sticky="ew")

saborLb = tk.Label(text="Sabor:", font=("Times New Roman", 14))
saborLb.grid(padx=5, pady=7, column=0, row=2, sticky="w")
saborEt = tk.Entry()
saborEt.grid(padx=5, pady=7, column=1, row=2, columnspan=2, sticky="ew")

tipoPrecoLb = tk.Label(text="Tipo de Preço (Responder (Kg) ou (unidade)):", font=("Times New Roman", 14))
tipoPrecoLb.grid(padx=5, pady=7, column=0, row=3, sticky="w")
tipoPrecoEt = tk.Entry()
tipoPrecoEt.grid(padx=5, pady=7, column=1, row=3, columnspan=2, sticky="ew")

precoLb = tk.Label(text="Preço:", font=("Times New Roman", 14))
precoLb.grid(padx=5, pady=7, column=0, row=4, sticky="w")
precoEt = tk.Entry()
precoEt.grid(padx=5, pady=7, column=1, row=4, columnspan=2, sticky="ew")

disponivelLb = tk.Label(text="Está disponível? (Sim ou não)", font=("Times New Roman", 14))
disponivelLb.grid(padx=5, pady=7, column=0, row=5, sticky="w")
disponivelEt = tk.Entry()
disponivelEt.grid(padx=5, pady=7, column=1, row=5, columnspan=2, sticky="ew")

limparBt = tk.Button(text="Limpar", font=("Times New Roman", 14), command=limparCampos)
limparBt.grid(padx=5, pady=7, column=1, row=6,  sticky="ew")
salvarBt = tk.Button(text="Salvar", font=("Times New Roman", 14), command=cadastrarTipo)
salvarBt.grid(padx=5, pady=7, column=2, row=6,  sticky="ew")

tiposDeDocesCad = tk.Listbox(janela, width=30, height=10)
tiposDeDocesCad.grid(padx=5, pady=7, column=0, row=7, columnspan=3, sticky="ew")
# Seleciona a lista de tipos de doces.
tiposCad = TipoDoce.select()
# Mostra todos os atributos de cada tipo de doce.
for doce in tiposCad:
    tiposDeDocesCad.insert(tk.END, f"(ID: {doce.id})")
    tiposDeDocesCad.insert(tk.END, f"Classificação: {doce.classificacao}")
    tiposDeDocesCad.insert(tk.END, f"Sabor: {doce.sabor}")
    if doce.tipoPreco:
        tiposDeDocesCad.insert(tk.END, f"O preço do doce por unidade é R${doce.preco}")
    else:
        tiposDeDocesCad.insert(tk.END, f"O preço do doce por kg é R${doce.preco}")
    if doce.disponivel:
        tiposDeDocesCad.insert(tk.END, f"O doce está disponível.")
    else: 
        tiposDeDocesCad.insert(tk.END, f"O doce não está disponível.")
    tiposDeDocesCad.insert(tk.END, "\n--------------------------------------------------------------------------------------------------\n")

editarBt = tk.Button(text="Editar", font=("Times New Roman", 14), command=editarTipo)
editarBt.grid(padx=5, pady=7, column=0, row=8,  sticky="ew")
excluirBt = tk.Button(text="Excluir", font=("Times New Roman", 14))
excluirBt.grid(padx=5, pady=7, column=1, row=8,  sticky="ew")


janela.mainloop()