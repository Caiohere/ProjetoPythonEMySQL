from tkinter import *
from tkinter import ttk



def tabela():
    from mysql.connector import connect

    def mysql_connection(host, user, password, database=None):
        connections = connect(host=host, user=user, password=password, database=database)
        return connections

    connection = mysql_connection('aws.connect.psdb.cloud', 'youot82v69bmjtdew633', 'pscale_pw_xH95meWuJiFkwf9c57Lf49q09rBSikUSOgSmLS78nMK', 'projetocad')

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

    labelavisos = Label(window2, text="OBS: RETORNE PARA A PAGINA DE CADASTRO PARA ADICIONAR"
                                      "\n OUTROS PRODUTOS AO BANCO DE DADOS", bg="#00BFFF", foreground='black', font=15)
    labelavisos.place(x=180, y=260)

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
    tabelaview.pack()

    lista = []
    tabelaview.insert("", END, values=lista)

    for i, c in enumerate(result):
        cola = result[i]
        tabelaview.insert("", END, values=cola)

    window2.mainloop()