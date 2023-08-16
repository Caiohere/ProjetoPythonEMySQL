from tkinter import *
from tkinter import ttk
from TableWindow import tabela

def mainprog():
    window = Tk()
    window.geometry("800x400")
    window.title("ProjetoCAD - Cadastro de Produtos")
    window.configure(background='#00BFFF')


    label = Label(window, text="CADASTRO", bg="#00BFFF", font=("Segoe IU", 15))
    label.place(x=330, y=20)

    label1 = Label(window, text="Código", bg="#00BFFF", pady=10, padx=10, font=("Segoe IU", 15))
    label1.place(x=25, y=50)

    label2 = Label(window, text="Produto", bg="#00BFFF", pady=10, padx=10, font=("Segoe IU", 15))
    label2.place(x=25, y=110)

    label3 = Label(window, text="Preço", bg="#00BFFF", pady=10, padx=10, font=("Segoe IU", 15))
    label3.place(x=25, y=170)

    label4 = Label(window, text="", bg="#00BFFF", foreground="red", font=10)
    label4.place(x=280, y=90)

    label5 = Label(window, text="", bg="#00BFFF", foreground="green", font=10)
    label5.place(x=300, y=110)


    entry = Entry(window, width=30)
    entry.place(x=40, y=90)

    entry1 = Entry(window, width=30)
    entry1.place(x=40, y=150)

    entry2 = Entry(window, width=30)
    entry2.place(x=40, y=210)


    radios = StringVar()
    radio = Radiobutton(text="Alimento", bg="#00BFFF", font=15, value=f"\'alimento\'", variable=radios)
    radio.place(x=40, y=300)

    radio2 = Radiobutton(text="Têxtil", bg="#00BFFF", font=15, value=f"\'têxtil\'", variable=radios)
    radio2.place(x=160, y=300)

    radio3 = Radiobutton(text="Eletrônico", bg="#00BFFF", font=15, value=f"\'eletrônico\'", variable=radios)
    radio3.place(x=280, y=300)


    def getentry():
        def inserir():
            from mysql.connector import connect

            def mysql_connection(host, user, password, database=None):
                connections = connect(host=host, user=user, password=password, database=database)
                return connections

            connection = mysql_connection('aws.connect.psdb.cloud', 'youot82v69bmjtdew633', 'pscale_pw_xH95meWuJiFkwf9c57Lf49q09rBSikUSOgSmLS78nMK', 'projetocad')

            command = f'''insert into Lojinha(Codigo, Produto, Preco, Categoria)
            values({text1}, {text2}, {text3}, {radselect})'''

            query = f'''
                {command}
            '''
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

        #OBTENÇAO DOS DADOS
        text1 = entry.get()
        text2 = entry1.get()
        text3 = entry2.get()
        try:
            text1 = int(text1)
        except ValueError:
            erro1 = 1
            print(text1, erro1)
        else:
            erro1 = 0
            print(text1)

        teste = text2.isalpha()
        if not teste:
            erro2 = 1
            print(text2, erro2)
        else:
            text2 = f"\'{text2}\'"
            erro2 = 0
            print(text2)

        try:
            text3 = float(text3)
        except ValueError:
            erro3 = 1
            print(text3, erro3)
        else:
            erro3 = 0
            print(text3)
        #analise de erros
        radselect = radios.get()
        if len(radselect) == 0:
            erro4 = 1
        else:
            erro4 = 0
        print(radselect)
        if erro1 or erro2 or erro3 or erro4 == 1:
            label5["text"] = ''
            label4["text"] = 'Erro! Verifique se todos os campos foram selecionados corretamente.'
        else:
            inserir()
            label4["text"] = ''
            label5["text"] = 'Produto cadastrado com sucesso!'


    button1 = Button(window, text="ENVIAR", command=getentry, padx=35, pady=10, font="Arial")
    button1.place(x=440, y=300)

    button2 = Button(window, text="ABRIR TABELA", command=tabela, padx=35, pady=10, font="Arial")
    button2.place(x=600, y=300)

    window.mainloop()
