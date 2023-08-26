from tkinter import *
from tkinter import ttk
from TableWindow import table
from functions import getentry, mysql_connection, input_tree, refresh

def mainprog():
    connection = mysql_connection('aws.connect.psdb.cloud', '6fiid5c42zyaspmwasqt', 'pscale_pw_ABoWRpuJNYN9MvniFj1PY3YyfvkCSD4xIuMJbCOdsOq', 'projetocad')

    command = 'select * from Lojinha'

    query = f'''
        {command}
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    result1 = cursor.fetchall()


    window = Tk()
    window.geometry("800x400")
    window.title("ProjetoCAD - Cadastro de Produtos")
    window.configure(background='#00BFFF')


    label = Label(window, text="CADASTRO", bg="#00BFFF", font=("Segoe IU", 15))
    label.place(x=15, y=15)

    label1 = Label(window, text="Código", bg="#00BFFF", pady=10, padx=10, font=("Segoe IU", 15))
    label1.place(x=25, y=50)

    label2 = Label(window, text="Produto", bg="#00BFFF", pady=10, padx=10, font=("Segoe IU", 15))
    label2.place(x=25, y=110)

    label3 = Label(window, text="Preço", bg="#00BFFF", pady=10, padx=10, font=("Segoe IU", 15))
    label3.place(x=25, y=170)

    label4 = Label(window, text="", bg="#00BFFF", foreground="red", font=10)
    label4.place(x=310, y=250)

    #label5 = Label(window, text="", bg="#00BFFF", foreground="green", font=10)
    #label5.place(x=300, y=250)


    entry = Entry(window, width=30)
    entry.place(x=40, y=90)

    entry1 = Entry(window, width=30)
    entry1.place(x=40, y=150)

    entry2 = Entry(window, width=30)
    entry2.place(x=40, y=210)


    radios = StringVar()
    radio = Radiobutton(text="Alimento", bg="#00BFFF", font=15, value=f"\'alimento\'", variable=radios)
    radio.place(x=40, y=250)

    radio2 = Radiobutton(text="Têxtil", bg="#00BFFF", font=15, value=f"\'têxtil\'", variable=radios)
    radio2.place(x=40, y=280)

    radio3 = Radiobutton(text="Eletrônico", bg="#00BFFF", font=15, value=f"\'eletrônico\'", variable=radios)
    radio3.place(x=40, y=310)
    global tabelaview1
    tabelaview1 = ttk.Treeview(window,  selectmode='browse',
                              columns=("Código", "Produto", "Preço", "Categoria"), show='headings')

    tabelaview1.column("Código", width=50, minwidth=50)
    tabelaview1.heading("Código", text="Código")
    tabelaview1.column("Produto", width=150, minwidth=100)
    tabelaview1.heading("Produto", text="Produto")
    tabelaview1.column("Preço", width=100, minwidth=70)
    tabelaview1.heading("Preço", text="Preço")
    tabelaview1.column("Categoria", width=150, minwidth=100)
    tabelaview1.heading("Categoria", text="Categoria")
    tabelaview1.place(x=340, y=15)



    def opengetentry():
        text1 = entry.get()
        text2 = entry1.get()
        text3 = entry2.get()
        radselect = radios.get()
        getentry(text1,text2, text3, radselect, label4)
        refresh(tabelaview1)
    
    def openrefresh():
        refresh(tabelaview1)
        label4["text"] = 'Tabela atualizada!'
        label4["foreground"] = "green"
            

    input_tree(result1, tabelaview1)



    button1 = Button(window, text="ENVIAR", command=opengetentry, padx=35, pady=10, font="Arial")
    button1.place(x=340, y=300)

    button2 = Button(window, text="ABRIR TABELA", command=table, padx=15, pady=10, font="Arial")
    button2.place(x=630, y=300)

    button3 = Button(window, text="ATUALIZAR", command=openrefresh, padx=15, pady=10, font="Arial")
    button3.place(x=492, y=300)

    window.mainloop()
