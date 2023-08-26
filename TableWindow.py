from tkinter import *
from tkinter import ttk
from functions import input_tree, mysql_connection, update, delete


def table():
    connection = mysql_connection('aws.connect.psdb.cloud', '6fiid5c42zyaspmwasqt', 'pscale_pw_ABoWRpuJNYN9MvniFj1PY3YyfvkCSD4xIuMJbCOdsOq', 'projetocad')

    command = 'select * from Lojinha'

    query = f'''
        {command}
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    window2 = Toplevel()
    window2.geometry("800x400")
    window2.title("ProjetoCAD - Tabela")
    window2.configure(background='#00BFFF')
    window2.grab_set()

    tabelaview = ttk.Treeview(window2,  selectmode='browse',
                              columns=("Código", "Produto", "Preço", "Categoria"), show='headings')

    tabelaview.column("Código", width=50, minwidth=50)
    tabelaview.heading("Código", text="Código")
    tabelaview.column("Produto", width=150, minwidth=100)
    tabelaview.heading("Produto", text="Produto")
    tabelaview.column("Preço", width=100, minwidth=70)
    tabelaview.heading("Preço", text="Preço")
    tabelaview.column("Categoria", width=150, minwidth=100)
    tabelaview.heading("Categoria", text="Categoria")
    tabelaview.place(x=25, y=20)


    label = Label(window2, text="Atualizar Dados", bg="#00BFFF", font=("Segoe IU", 15))
    label.place(x=520, y=20)

    label1 = Label(window2, text="Código do produto: ", bg="#00BFFF", pady=0, padx=0, font=("Segoe IU", 12))
    label1.place(x=535, y=55)

    label2 = Label(window2, text="Selecione a coluna: ", bg="#00BFFF", pady=0, padx=0, font=("Segoe IU", 12))
    label2.place(x=535, y=82)

    label3 = Label(window2, text="Nova informação: ", bg="#00BFFF", pady=0, padx=0, font=("Segoe IU", 12))
    label3.place(x=535, y=110)

    label4 = Label(window2, text="", bg="#00BFFF", pady=0, padx=0, font=("Segoe IU", 12), foreground="red")
    label4.place(x=50, y=255)

    label5 = Label(window2, text="Deletar dados", bg="#00BFFF", font=("Segoe IU", 15))
    label5.place(x=520, y=210)

    label6 = Label(window2, text="Código do produto: ", bg="#00BFFF", pady=0, padx=0, font=("Segoe IU", 12))
    label6.place(x=535, y=245)


    n = StringVar()
    column_choosen = ttk.Combobox(window2, width=15, textvariable=n)
    column_choosen['values'] = ('Produto',
                                'Preço',
                                'Categoria')
    column_choosen.place(x=675, y=82)
    column_choosen.current()

    entry = Entry(window2, width=15)
    entry.place(x=675, y=55)

    entry2 = Entry(window2, width=18)
    entry2.place(x=675, y=110)

    entry3 = Entry(window2, width=15)
    entry3.place(x=675, y=245)

    def openupdate():
        from MainProg import tabelaview1
        input = entry.get()
        input2 = entry2.get()
        combo = column_choosen.get()
        update(input, input2, combo, label4, tabelaview)
        
    def opendelete():
        from MainProg import tabelaview1
        input3 = entry3.get()
        delete(input3, label4, tabelaview)
    
    input_tree(result, tabelaview)

    button = Button(window2, text="Atualizar", command=openupdate, padx=35, pady=10, font="Arial")
    button.place(x=585, y=138)

    button1 = Button(window2, text="Deletar", command=opendelete, padx=35, pady=10, font="Arial")
    button1.place(x=585, y=280)

    window2.mainloop()