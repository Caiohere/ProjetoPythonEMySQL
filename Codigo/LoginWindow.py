from tkinter import *
from tkinter import ttk
from MainProg import mainprog
from functions import open

def loginwindow():
    login_window = Tk()
    login_window.geometry("800x400")
    login_window.title("ProjetoCAD - Login")
    login_window.configure(background='#00BFFF')
    login_window.resizable(False, False)


    #img = PhotoImage(file="usericon.png")
    #label = Label(login_window, image=img, borderwidth=0)
    #label.place(x=330, y=20)    

    label = Label(login_window, text="Usuário", bg="#00BFFF", pady=0, padx=0, font=("Segoe IU", 12), foreground="white")
    label.place(x=310, y=130)

    label1 = Label(login_window, text="Senha", bg="#00BFFF", pady=0, padx=0, font=("Segoe IU", 12), foreground="white")
    label1.place(x=310, y=185)

    label2 = Label(login_window, text="", bg="#00BFFF", pady=0, padx=0, font=("Segoe IU", 12), foreground="red")
    label2.place(x=230, y=240)

    label3 = Label(login_window, text="Desenvolvido por Caio :)\nVersion 0.3, 2023", bg="#00BFFF")
    label3.place(x=665, y=360)


    entry = Entry(login_window, width=30)
    entry.place(x=300, y=160)

    entry1 = Entry(login_window, width=30, show="*")
    entry1.place(x=300, y=210)

    users = ["Caio", ""]
    passwords = ["1234", ""]



    def useopen():
        user = entry.get()
        password = entry1.get()
        open(user, users, password, passwords, login_window, mainprog, label2)
        

    button_login = Button(login_window, text="ENTRAR", command=useopen, padx=35, pady=10, font="Arial")
    button_login.place(x=320, y=280)

    login_window.mainloop()
