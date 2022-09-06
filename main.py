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
        texto2['text'] = 'Selecione a operação'
    elif nValido:
        texto1['text'] = 'Digite o numero valido'
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
            tabuada += f"{numero}{operacao}{n}={resultado}\n"
            resultado = ""
            if operacao not in ["/"]:
                n +=1
        Resultado['text'] = tabuada
                
        


janela = Tk()
janela.title('Tabuada')
texto1 = Label(janela, text='Digite o valor para gerar a tabela')
texto1.grid(column=0, row=0)
numerotxt = Entry(janela, width=10)
numerotxt.grid(column=0, row=1)
texto2 = Label(janela, text='Selecione a operação para gerar a tabela')
texto2.grid(column=0, row=2)
botaoMais = Button(janela, text='+', command=mais, bg='white')
botaoMais.grid(column=0, row=3)
botaoMenos = Button(janela, text='-', command=menos, bg='white')
botaoMenos.grid(column=0, row=4)
botaoVezes = Button(janela, text='x', command=vezes, bg='white')
botaoVezes.grid(column=0, row=5)
botaoDividir = Button(janela, text='/', command=dividir, bg='white')
botaoDividir.grid(column=0, row=6)
botaoGerar = Button(janela, text='=', command=gerar, bg='white')
botaoGerar.grid(column=0, row=7)
auxiliar = Label()
Resultado = Label(janela)
Resultado.grid(column=1, row=0, rowspan=10)
       
janela.mainloop()