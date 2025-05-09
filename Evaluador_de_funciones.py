from tkinter import *
from math import *
import sympy as sp
import numpy as np

raiz = Tk()
raiz.title("Suma de dos números")
raiz.resizable(True,True)
#raiz.iconbitmap("unnamed.ico")

miFrame=Frame(raiz, width = 500 , height = 500)   #aqui indicamos el tamño de nuestra cajita
miFrame.pack()

lbl1 =Label(miFrame, text="Inserte un número: ") # para poner etiquetas
lbl1.place(x=10,y=10,width=100, height=30)

lbl2 =Label(miFrame, text="Inserte otro número ") # para poner etiquetas
lbl2.place(x=10,y=50,width=110, height=30)

cuad1 = Entry(miFrame)                         # para cuadros de texto
cuad1.place(x=130,y=10,width=100, height=30)

cuad2 = Entry(miFrame)                         # para cuadros de texto
cuad2.place(x=130,y=50,width=100, height=30)

cuad3 = Entry(miFrame)                         # para cuadros de texto
cuad3.place(x=130,y=90,width=100, height=30)

def codigoBoton():
    x = sp.symbols("x")
    b = C1.get()
    fn = sp.sympify(b) 
    f = sp.lambdify(x,fn)
    a = float(C2.get())
    c = f(a)
    C3.delete(0,END)
    C3.insert(0,c)

B3 = Button(miFrame, text="Evaluar" , command=codigoBoton)   #puede ser raiz o miframe
B3.place(x=90 , y =160)


    

raiz.mainloop()



