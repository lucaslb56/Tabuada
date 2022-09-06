from cgitb import text
import this
from turtle import textinput
import requests
from tkinter import *

def mais():  
    auxiliar['text'] = '+'
    botaoMais.configure(bg="blue")
    botaoMenos.configure(bg="white")
    botaoVezes.configure(bg="white")
    botaoDividir.configure(bg="white")
def menos():  
    auxiliar['text'] = '-'
    botaoMenos.configure(bg="blue")
    botaoMais.configure(bg="white")
    botaoVezes.configure(bg="white")
    botaoDividir.configure(bg="white")
def vezes():  
    auxiliar['text'] = 'x'
    botaoVezes.configure(bg="blue")
    botaoMais.configure(bg="white")
    botaoMenos.configure(bg="white")
    botaoDividir.configure(bg="white")
def dividir():  
    auxiliar['text'] = '/'
    botaoDividir.configure(bg="blue")
    botaoMais.configure(bg="white")
    botaoMenos.configure(bg="white")
    botaoVezes.configure(bg="white")

def gerar():
    operacao = auxiliar['text']
    try:
        numero = int(numerotxt.get())
        nValido = False
    except:
        nValido = True
    if  operacao == '':
        legenda['text'] = 'Selecione a operação'
    elif nValido:
        legenda['text'] = 'Digite o numero valido'
    else:
        n = 1
        tabuada = ""
        for i in range(1, 11):
            if operacao == "+":
                resultado = n + numero
            elif operacao == "-":
                if n < numero:
                    n = numero
                    resultado = n - numero
                else:
                    resultado = n - numero
            elif operacao == "x":
                resultado = n * numero
            else:
                if n < numero:
                    n = numero
                else:
                    if n == 1 and i == 1:
                        n = 1
                    else:
                        n += numero
                resultado = n / numero
                resultado = int(resultado)
            tabuada += f"{n} {operacao} {numero} = {resultado}\n"
            resultado = ""
            if operacao not in ["/"]:
                n +=1
        Resultado['text'] = tabuada
                
        


janela = Tk()
janela.minsize(270, 240)
janela.title('Tabuada')
#Linha 0 Titulo
legenda = Label(janela, text='TABUADA', width=40, bg='#4682B4')
legenda.grid(column=0, row=0, columnspan=4)
#Linha 1 valor
txtovalor = Label(janela, text='VALOR', width=10)
txtovalor.grid(column=0, row=1, columnspan=1)
numerotxt = Entry(janela, width=12)
numerotxt.grid(column=1, row=1)
#Linha 2 botoes
botaoMais = Button(janela, text='+', command=mais, bg='white', width=10, height=3)
botaoMais.grid(column=0, row=2)
botaoMenos = Button(janela, text='-', command=menos, bg='white', width=10, height=3)
botaoMenos.grid(column=1, row=2)
#Linha 3 botoes
botaoVezes = Button(janela, text='x', command=vezes, bg='white', width=10, height=3)
botaoVezes.grid(column=0, row=3)
botaoDividir = Button(janela, text='/', command=dividir, bg='white', width=10, height=3)
botaoDividir.grid(column=1, row=3)
#Linha 4 gerar
botaoGerar = Button(janela, text='=', command=gerar, bg='white', width=22, height=3)
botaoGerar.grid(column=0, row=4, columnspan=2)
auxiliar = Label()
Resultado = Label(janela, bd=10, height=10, font=10, bg='#4169E1', width=10)
Resultado.grid(column=3, row=1, rowspan=4)
       
janela.mainloop()