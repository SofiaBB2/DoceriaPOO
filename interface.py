import tkinter as tk
from models import TipoDoce
from tkinter import messagebox as mb


def atualizaListbox():
    tiposDeDocesCad.delete(0, tk.END)

    tiposCad = TipoDoce.select()
    # Mostra todos os atributos de cada tipo de doce.
    for doce in tiposCad:
        tiposDeDocesCad.insert(tk.END, f"Classificação: {doce.classificacao} (ID: {doce.id})")
        tiposDeDocesCad.insert(tk.END, f"Sabor: {doce.sabor} (ID: {doce.id})")
        if doce.tipoPreco:
            tiposDeDocesCad.insert(tk.END, f"O preço do doce por unidade é R${doce.preco} (ID: {doce.id})")
        else:
            tiposDeDocesCad.insert(tk.END, f"O preço do doce por kg é R${doce.preco} (ID: {doce.id})")
        if doce.disponivel:
            tiposDeDocesCad.insert(tk.END, f"O doce está disponível. (ID: {doce.id})")
        else: 
            tiposDeDocesCad.insert(tk.END, f"O doce não está disponível. (ID: {doce.id})")
        tiposDeDocesCad.insert(tk.END, "\n--------------------------------------------------------------------------------------------------\n")


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
    if (tipoPreco.casefold() == "unidade"):
        tipoPreco = True
    elif(tipoPreco.casefold() == "kg"):
        tipoPreco = False
    else:
        mb.showerror("Erro em Tipo de Preço", "Informe um valor válido! ('Kg' ou 'unidade')")

    try:
        preco = float(precoEt.get())
    except:
        mb.showerror("Erro em Preço", "Informe um valor válido! (algum valor numérico)")

    disponivel = disponivelEt.get()
    if (disponivel.casefold() == "sim"):
        disponivel = True
    else:
        disponivel = False

    # Cadastra o objeto no BD.
    tipoCad = TipoDoce.create(classificacao=classificacao, sabor=sabor, tipoPreco=tipoPreco, preco=preco, disponivel=disponivel)

    limparCampos()
    atualizaListbox()

    mb.showinfo("Cadastro concluído", "Cadastrado com sucesso!")

def pegarSelecao():
    selecao = tiposDeDocesCad.curselection()
    if selecao: 
        indice = selecao[0]
        texto = tiposDeDocesCad.get(indice)
        texto = texto.split("ID: ")
        idAt = texto[1].replace(")", "")
        return idAt
    else:
        return -1

def editarTipo():
    idAt = int(pegarSelecao())
    tipoAt = TipoDoce.get(TipoDoce.id == idAt)

    classificacaoEt.delete(0, tk.END)
    classificacaoEt.insert(0, tipoAt.classificacao)

    saborEt.delete(0, tk.END)
    saborEt.insert(0, tipoAt.sabor)

    tipoPrecoEt.delete(0, tk.END)
    tipoPrecoEt.insert(0, tipoAt.tipoPreco)

    precoEt.delete(0, tk.END)
    precoEt.insert(0, tipoAt.preco)

    disponivelEt.delete(0, tk.END)
    disponivelEt.insert(0, tipoAt.disponivel)

    global salvarBt
    salvarBt.destroy()
    salvarBt = tk.Button(text="Alterar", font=("Times New Roman", 14), command=lambda: pegaNovosVal(tipoAt))
    salvarBt.grid(padx=5, pady=7, column=2, row=6,  sticky="ew")   


def pegaNovosVal(tipoAt):
    tipoAt.classificacao = classificacaoEt.get()
    tipoAt.sabor = saborEt.get()
    tipoPreco = tipoPrecoEt.get()
    if (tipoPreco.casefold() == "unidade".casefold() or tipoPreco == "1"):
        tipoAt.tipoPreco = True
    elif(tipoPreco.casefold() == "Kg".casefold() or tipoPreco == "0"):
        tipoAt.tipoPreco = False
    else:
        mb.showerror("Erro em Tipo de Preço", "Informe um valor válido! ('Kg' ou 'unidade')")
    try:
        tipoAt.preco = float(precoEt.get())
    except:
        mb.showerror("Erro em Preço", "Informe um valor válido! (algum valor numérico)")

    disponivel = disponivelEt.get()
    if (disponivel.casefold() == "sim".casefold() or disponivel == 1):
        tipoAt.disponivel = True
    else:
        tipoAt.disponivel = False
    tipoAt.save()
    atualizaListbox()
    limparCampos()
    global salvarBt
    salvarBt.destroy()
    salvarBt = tk.Button(text="Salvar", font=("Times New Roman", 14), command=cadastrarTipo)
    salvarBt.grid(padx=5, pady=7, column=2, row=6,  sticky="ew")
    
def excluirTipo():
    idExcluir = pegarSelecao()
    tipoEx = TipoDoce.get(TipoDoce.id == idExcluir)
    tipoEx.delete_instance()
    mb.showinfo("Excluído", "Tipo de Doce removido do banco de dados")
    atualizaListbox()


janela = tk.Tk("Doceria POO")
janela.geometry("520x550")

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

atualizaListbox()

editarBt = tk.Button(text="Editar", font=("Times New Roman", 14), command=editarTipo)
editarBt.grid(padx=5, pady=7, column=0, row=8,  sticky="ew")
excluirBt = tk.Button(text="Excluir", font=("Times New Roman", 14), command=excluirTipo)
excluirBt.grid(padx=5, pady=7, column=1, row=8,  sticky="ew")

janela.mainloop()