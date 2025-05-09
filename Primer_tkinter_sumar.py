from tkinter import *
from math import *

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
    a = float(cuad1.get())
    b = float(cuad2.get())
    c = a + b
    cuad3.delete(0,END)
    cuad3.insert(0,c)

botonEnvio = Button(raiz, text="Sumar" , command=codigoBoton)
botonEnvio.place(x=90 , y =160)


    

raiz.mainloop()

