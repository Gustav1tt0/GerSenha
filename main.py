import random
import tkinter
from tkinter import *
root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.janela()
        self.dados()
        root.mainloop()
    def janela(self):
        self.root.title("Gerador de senhas")
        self.root.configure(background= 'grey10')
        self.root.geometry("400x400")
        self.root.resizable(True, True)
    def dados(self):

        ## Criação da label e entrada do Quantidade de caracteres
        self.quantcare = IntVar()
        self.lb_quantcare1 = Label(text="Insira abaixo a quantidade de caracteres que deseja para criar sua senha ", bg='blue', fg='#00FFFF')
        self.lb_quantcare1.place(relx=0.02, rely=0.15)
        self.quantcare1_entry = Entry(textvariable=self.quantcare)
        self.quantcare1_entry.place(relx=0.40, rely=0.25, relwidth=0.12)
        # Resultado
        self.resultadogeral = StringVar()
        self.lb_resultado1 = Label()
        self.lb_resultado1.place(relx=0.35, rely=0.35)
        self.resultado1 = Label(textvariable=self.resultadogeral)
        self.resultado1.place(relx=0.31, rely=0.35, relwidth=0.3)

        ### Criação do botao Gerar senha
        self.bt_geralsenha1 = Button(text="Gerar senha", bd=2, bg='blue', fg='#00FFFF'
                                , font=('verdana', 8, 'bold'), command=self.gerarsenha)
        self.bt_geralsenha1.place(relx=0.31, rely=0.50, relwidth=0.3, relheight=0.1)
    def gerarsenha(self):
        num_caract = self.quantcare.get()
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%_-\/¨&*'
        passwd = ""
        while len(passwd) != num_caract:
            passwd = passwd + random.choice(char_list)
        return self.resultadogeral.set(passwd)

Application()