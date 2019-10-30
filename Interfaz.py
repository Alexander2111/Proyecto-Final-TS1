#Importar librerias 
import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

ventana = Tk()

n = random.randint(1,100)

##Pares
#Ventana de pares 
def abrir_ventana2():
    etiquetaPares1 = Label(ventana, text=">>>>>>>> PARES <<<<<<<<",fg="blue",bg="#48C9B0").place(x=90, y=190)
    etiquetaPares2 = Label(ventana, text="Recuerde:",fg="blue",bg="#48C9B0").place(x=60, y=220)
    etiquetaPares3 = Label(ventana, text="Un numero es par si se puede ser dividio entre 2",fg="blue",bg="#48C9B0").place(x=60, y=240)
    etiquetaPares4 = Label(ventana, text="Coloque Si,si desea seguir.",fg="blue",bg="#48C9B0").place(x=60, y=260)
    etiquetaPares5 = Label(ventana, text="Coloque No,si desea acabar.",fg="blue",bg="#48C9B0").place(x=60, y=280)
#Botones Pares 
    botonPA1 = Button(ventana, text="Inicar Juego", command=sacar,activebackground="red").place(x=80, y=350)
#Definicion de Botones Pares
def sacar():
    messagebox.showinfo("Mensaje", "Debe de registrar al menos a 2 jugadores :D")

##Impares
#Ventana Impares 
def abrir_ventana3():
    etiquetaIPares1 = Label(ventana, text=">>>>>>>> PARES <<<<<<<<",fg="blue",bg="#48C9B0").place(x=90, y=190)
    etiquetaIPares2 = Label(ventana, text="Recuerde:",fg="blue",bg="#48C9B0").place(x=60, y=220)
    etiquetaIPares3 = Label(ventana, text="Un numero es impar si no puede ser dividio entre 2",fg="blue",bg="#48C9B0").place(x=60, y=240)
    etiquetaIPares4 = Label(ventana, text="Coloque Si,si desea seguir.",fg="blue",bg="#48C9B0").place(x=60, y=260)
    etiquetaIPares5 = Label(ventana, text="Coloque No,si desea acabar.",fg="blue",bg="#48C9B0").place(x=60, y=280)
#Botones Impares 
    botoniPA1 = Button(ventana, text="Inicar Juego", command=sacarIMP,activebackground="red").place(x=80, y=350)
#Definicion de botones impares

##Primos
# #Ventana Primos
def abrir_ventana4():
    etiqueta3 = Label(ventana, text=">>>>>>>> PRIMOS <<<<<<<<",fg="blue",bg="#48C9B0").place(x=90, y=190)

##Multiplicar
#Ventana tabala de multiplicar
def abrir_ventana5():
    etiqueta3 = Label(ventana, text=">>>>>>>> MULTIPLICAR <<<<<<<<",fg="blue",bg="#48C9B0").place(x=90, y=190)

#Diseño de la Interfaz (Ventana 1)
ventana.geometry('350x480')
ventana.title(" CHIQUIMATEANDO")
etiqueta = Label(ventana, text="Bienvenidos a CHIQUIMATEANDO",bg="#48C9B0")
etiqueta.pack()
ventana.config (bg="#48C9B0")
ttk.Button(ventana, text='Salir', command=ventana.destroy).pack(side=BOTTOM)


#Interfaz Botones 

boton1 = Button(ventana, text="Pares",command=abrir_ventana2,activebackground="#369A8E").place(x=70, y=130)
boton2 = Button(ventana, text="Impares",command=abrir_ventana3,activebackground="#369A8E").place(x=185, y=130)
boton3 = Button(ventana, text="Primos", command=abrir_ventana4,activebackground="#369A8E").place(x=60, y=90)
boton4 = Button(ventana, text="Tabla de multiplicar", command=abrir_ventana5,activebackground="#369A8E").place(x=180, y=90)


ventana.mainloop()