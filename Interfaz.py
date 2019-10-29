#Importar librerias 
import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

ventana = Tk()
#Definimos numeros 
n = []

#Numero salidos 
m = []

#Diseño de la Interfaz (Ventana 1)
ventana.geometry('350x480')
ventana.title(" CHIQUIMATEANDO")
etiqueta = Label(ventana, text="Bienvenidos a CHIQUIMATEANDO",bg="#48C9B0")
etiqueta.pack()
ventana.config (bg="#48C9B0")
ttk.Button(ventana, text='Salir', command=ventana.destroy).pack(side=BOTTOM)



#Interfaz Botones 


ventana.mainloop()