#Function usada na function getentry(functions.py)
def primary_count(entry):
    connection = mysql_connection('aws.connect.psdb.cloud', 'avb4xvpusmcmmmn1g4r5', 'pscale_pw_LqcGb6bWIWSkMMXiId0fc8lIuuG36ykXtkWRN7i9wsz', 'projetocad')

    command = f'select count(*) from Lojinha where Codigo = {entry}'

    query = f'''
        {command}
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    if result[0][0] == 1:
        return 1
    else:
        return 2
    
#function usada no LoginWindow.py
def open(user, users, password, passwords, window, function, label):
    if user in users and password in passwords:
        window.destroy()
        function()
    else:
        label["text"] = 'Usuário ou senha incorreto(s), Digite novamente.'

#function usada na function getentry(functions.py)
def inserir(text1, text2, text3, radselect):
            connection = mysql_connection('aws.connect.psdb.cloud', 'avb4xvpusmcmmmn1g4r5', 'pscale_pw_LqcGb6bWIWSkMMXiId0fc8lIuuG36ykXtkWRN7i9wsz', 'projetocad')

            command = f'''insert into Lojinha(Codigo, Produto, Preco, Categoria)
            values({text1}, {text2}, {text3}, {radselect})'''

            query = f'''
                {command}
            '''
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()

#Function usada no MainProg.py
def getentry(text1,text2, text3, radselect, label4):
        #OBTENÇAO DOS DADOS
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
        if len(radselect) == 0:
            erro4 = 1
        else:
            erro4 = 0
        print(radselect)
        if erro1 or erro2 or erro3 or erro4 == 1:
            label4["text"] = 'Erro! Verifique se todos os campos foram selecionados corretamente.'
            label4["foreground"] = "red"
        elif primary_count(text1) == 1:
            label4["text"] = 'Erro! Produto com o mesmo código já adicionado.'
            label4["foreground"] = "red"
        else:
            inserir(text1, text2, text3, radselect)
            label4["text"] = 'Produto cadastrado com sucesso!'
            label4["foreground"] = "green"

#Function usada em diversas partes do sistema
def mysql_connection(host, user, password, database=None):
    from mysql.connector import connect
    connections = connect(host=host, user=user, password=password, database=database)
    return connections

#Function usada no MainProg.py e TableWindow
def input_tree(list, treeview):
    from tkinter import END
    for i, c in enumerate(list):
        cola = list[i]
        treeview.insert("", END, values=cola)

#Function usada no MainProg.py e dentro de outras functions
def refresh(treeview):
    from tkinter import END
    for i in treeview.get_children():
        treeview.delete(i)
    connection = mysql_connection('aws.connect.psdb.cloud', 'avb4xvpusmcmmmn1g4r5', 'pscale_pw_LqcGb6bWIWSkMMXiId0fc8lIuuG36ykXtkWRN7i9wsz', 'projetocad')

    command = 'select * from Lojinha'

    query = f'''
        {command}
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    lista = []
    treeview.insert("", END, values=lista)
    for i, c in enumerate(result):
        cola = result[i]
        treeview.insert("", END, values=cola)

#Function usada na TableWindow.py
def update(input, input2, combo, label, treeview):
    erro1 = 0
    erro2 = 0
    erro3 = 0
    erro4 = 0
    erro5 = 0
    try:
        input = int(input)
    except ValueError:
        erro1 = 1
        print("erro 1")
    else:
        erro1 = 0
    if primary_count(input) == 2:
        erro1 = 1
    else:
        erro1 = 0
    if combo == "Produto" or combo == "Categoria":
        teste = input2.isalpha()
        if not teste:
            erro2 = 1
            print("erro 2")
        else:
            erro2 = 0
    if combo == "Preço":
        try:
            input2 = float(input2)
        except ValueError:
            erro3 = 1
            print("erro 3")
        else:
            erro3 = 0
    if combo == "Categoria":
        list = ["Eletrônico", "eletrônico", "Têxtil", "têxtil", "Alimento", "alimento"]
        if input2 not in list:
            print(input2)
            print("Erro5")
            erro5 = 1
        else:
            erro5 = 0
    if combo != "Produto" and combo != "Preço" and combo != "Categoria":
            erro4 = 1
            print("erro 4")
    if erro1 or erro2 or erro3 or erro4 or erro5 == 1:
        print("erro")
        label["text"] = 'Erro na entrada das informações, por favor digite dados válidos '
        label["foreground"] = "red"
    else:
        label["text"] = 'Dado atualizado com sucesso!'
        label["foreground"] = "green"
        connection = mysql_connection('aws.connect.psdb.cloud', 'avb4xvpusmcmmmn1g4r5', 'pscale_pw_LqcGb6bWIWSkMMXiId0fc8lIuuG36ykXtkWRN7i9wsz', 'projetocad')

        if combo == "Produto":
            command = f'''UPDATE Lojinha set Produto = "{input2}" WHERE Codigo = {input};'''
        elif combo == "Preço":
            command = f'''UPDATE Lojinha set Preco = {input2} WHERE Codigo = {input};'''
        else:
            command = f'''UPDATE Lojinha set Categoria = "{input2}" WHERE Codigo = {input};'''
        query = f'''
            {command}
        '''
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        refresh(treeview)

#Function usada na TableWindow.py
def delete(input, label, treeview1):
    erro1 = 0
    erro2 = 0
    try:
        input = int(input)
    except ValueError:
        erro1 = 1
        label["text"] = 'Erro na entrada do Codigo, por favor digite dados válidos.'
        label["foreground"] = "red"
    else:
        erro1 = 2
    if primary_count(input) == 2:
        erro2 = 1
        label["text"] = "Erro! Código digitado não encontrado."
        label["foreground"] = "red"
    else:
        erro2 = 2
    print(erro1)
    print(erro2)
    if erro1 and erro2 == 2:
        label["text"] = 'Dados deletados com sucesso!'
        label["foreground"] = "green"
        connection = mysql_connection('aws.connect.psdb.cloud', 'avb4xvpusmcmmmn1g4r5', 'pscale_pw_LqcGb6bWIWSkMMXiId0fc8lIuuG36ykXtkWRN7i9wsz', 'projetocad')
        
        command = f'''DELETE from Lojinha where Codigo = {input}'''

        query = f'''
            {command}
        '''
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        refresh(treeview1)