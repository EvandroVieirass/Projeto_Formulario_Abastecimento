# importando tkinter

from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
# importando views

from view import *

# cores ###############p
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# criando janela

janela = Tk()
janela.title('Formulário de Abastecimento')
janela.geometry('1040x453')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

# dividindo a tela

frame_cima = Frame(janela, width=310, height=50, bg=co6, relief='flat')
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=403, bg=co9, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)
frame_direita = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# label cima

app_nome = Label(frame_cima, text='Formulário de Abastecimento',
                 anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

global tree

# função inserir

def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    data = e_data.get()
    combustivel = tipo_com.get()
    observacao = e_observacoes.get()
    lista = [nome, email, telefone, data, combustivel, observacao]
    if nome == "":
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserir_informacao(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_data.delete(0, 'end')
        e_observacoes.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrar()

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor_id = treev_lista[0]
        e_nome.insert(0, treev_lista[1])
        e_email.insert(0, treev_lista[2])
        e_telefone.insert(0, treev_lista[3])
        e_data.insert(0, treev_lista[4])
        e_observacoes.insert(0, treev_lista[6])

        def atualizar_informacao():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            data = e_data.get()
            combustivel = tipo_com.get()
            observacao = e_observacoes.get()
            lista = [nome, email, telefone, data,
                     combustivel, observacao, valor_id]
            if nome == "":
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo(
                    'Sucesso', 'Os dados foram atualizados com sucesso')
                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_telefone.delete(0, 'end')
                e_data.delete(0, 'end')
                e_observacoes.delete(0, 'end')
                b_confirmar.destroy()

                for widget in frame_direita.winfo_children():
                    widget.destroy()
                mostrar()
        b_confirmar = Button(frame_baixo, text='Confirmar', command=atualizar_informacao, width=7,  # ouverrelif muda de estilo
                             anchor=CENTER, font=('Ivy 12 bold'), fg=co1, bg=co2, relief='raised', overrelief='solid')
        b_confirmar.place(x=115, y=360)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona algum dos dados da tabela')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor_id = treev_lista[0]

        deletar_info([valor_id])
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
        for widget in frame_direita.winfo_children():
            widget.destroy()
        mostrar()
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona algum dos dados da tabela')

# frame baixo

l_nome = Label(frame_baixo, text='Nome *', anchor=NW,
               font=('Ivy 10 bold'), bg=co9, fg=co4, relief='flat')
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=50)

l_email = Label(frame_baixo, text='Telefone *', anchor=NW,
                font=('Ivy 10 bold'), bg=co9, fg=co4, relief='flat')
l_email.place(x=10, y=80)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=110)

l_telefone = Label(frame_baixo, text='Email *', anchor=NW,
                   font=('Ivy 10 bold'), bg=co9, fg=co4, relief='flat')
l_telefone.place(x=10, y=140)
e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=170)

tipo_com = StringVar()
l_combustivel = Label(frame_baixo, text='Combustivel *', anchor=NW,
                      font=('Ivy 10 bold'), bg=co9, fg=co4, relief='flat')
l_combustivel.place(x=180, y=200)
avgas = Radiobutton(frame_baixo, text="Avgas", value="Avgas",
                    anchor=NW, font=('Ivy 10'), bg=co9, variable=tipo_com)
avgas.place(x=180, y=220)
jet = Radiobutton(frame_baixo, text="Jet A1", value="Jet A1",
                  anchor=NW, font=('Ivy 10'), bg=co9, variable=tipo_com)
jet.place(x=180, y=240)

l_data = Label(frame_baixo, text='Data do Abastecimento *',
               anchor=NW, font=('Ivy 10 bold'), bg=co9, fg=co4, relief='flat')
l_data.place(x=10, y=200)
e_data = DateEntry(frame_baixo, width=17, background='skyblue',
                   foreground='white', bordercolor='skyblue', borderwidth=2)
e_data.place(x=15, y=230)

l_observacoes = Label(frame_baixo, text='Observações *', anchor=NW,
                      font=('Ivy 10 bold'), bg=co9, fg=co4, relief='flat')
l_observacoes.place(x=15, y=263)
e_observacoes = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_observacoes.place(x=15, y=283)

# botão inserir

b_inserir = Button(frame_baixo, text='Inserir', command=inserir, width=7,  # ouverrelif muda de estilo
                   anchor=CENTER, font=('Ivy 12 bold'), fg=co1, bg=co6, relief='raised', overrelief='solid')
b_inserir.place(x=15, y=320)

# botão atualizar

b_atualizar = Button(frame_baixo, text='Atualizar', command=atualizar, width=7,  # ouverrelif muda de estilo
                     anchor=CENTER, font=('Ivy 12 bold'), fg=co1, bg=co2, relief='raised', overrelief='solid')
b_atualizar.place(x=115, y=320)

# botão deletar

b_deletar = Button(frame_baixo, text='Deletar', command=deletar, width=7,  # ouverrelif muda de estilo
                   anchor=CENTER, font=('Ivy 12 bold'), fg=co1, bg=co7, relief='raised', overrelief='solid')
b_deletar.place(x=215, y=320)


# ------------------- codigo para tabela ----------------
def mostrar():
    global tree
    lista = mostrar_informacao()
    # lista para cabecario
    tabela_head = ['ID', 'Nome',  'email', 'telefone',
                   'Data', 'Tipo de Combutisvel', 'Observações']

    # criando a tabela

    tree = ttk.Treeview(frame_direita, selectmode="extended",
                        columns=tabela_head, show="headings")

    # vertical scrollbar

    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar

    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0, weight=12)
    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)


# mostrando tabela

mostrar()
janela.mainloop()
