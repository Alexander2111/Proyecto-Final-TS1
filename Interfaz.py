#Importar librerias 
import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

#Ventana
ventana = Tk()

#Interfaz 
nombre = StringVar()
etiqueta1 = Label(ventana, text="Nombre del Jugador(a,e): ",bg="#1887BF").place(x=40, y=35)
nombre_etiqueta = Entry(ventana, textvariable=nombre).place(x=180, y=35)
#Diseño de la Interfaz (Ventana 1)
ventana.geometry('350x300')
ventana.title(" CHIQUIMATEANDO")
etiqueta = Label(ventana, text="Bienvenidos a CHIQUIMATEANDO",bg="#1887BF",font=("Arial Bold",15))
etiqueta.pack() 
ventana.config (bg="#1887BF")
ttk.Button(ventana, text='Salir', command=ventana.destroy).pack(side=BOTTOM)

##NOmbre de Jugador
N=[]

##Ingreso nombre 
def in_name():
    if N.count(nombre.get()) == 0:
        N.append(nombre.get())
        messagebox.showinfo("Mensaje","Jugador Registrado Exitosamente")     
    else :
        messagebox.showinfo("Mensaje","Ya añadio un Jugador")
    nombre.set("")
    etiqueta12 = Label(ventana, text="Bienvenido(a,e)"+"  "+str(N[0]),bg="#1887BF").place(x=100, y=110)


###Diseño de la Interfaz (Ventana 2 (Pares))
##Ventana de pares 
def abrir_ventana2() :
    if int(len(N))>=1 :
        n = random.randint(1,100)
        #Definicion de Botones Pares
        def nofinal():
            messagebox.showinfo("Gracias","Gracias por jugar")
            ventana2.destroy()
        def yesfinal():
            messagebox.showinfo("Mensaje","Sigamos CHIQUIMATENANDO, Abra la ventana de nuevo")
            ventana2.destroy()
        def nop():
            if n % 2 != 0:
                etiquetaPares10 = Label(ventana2, text="Correcto.El numero ingresado no es par",fg="black",bg="#1887BF").place(x=250, y=310)
                etiquetaPares12 = Label(ventana2, text="Quieres seguir jugando?",fg="black",bg="#1887BF").place(x=280, y=330)
                BotonPAFSI = Button(ventana2, text="SI",command=yesfinal,activebackground="blue").place(x=300, y=370)
                BotonPAFNO = Button(ventana2, text="NO",command=nofinal,activebackground="blue").place(x=360, y=370)
            else:
                etiquetaPares11 = Label(ventana2, text="Incorrecto.El numero ingresado si es par",fg="black",bg="#1887BF").place(x=250, y=310)
                etiquetaPares12 = Label(ventana2, text="Quieres seguir jugando?",fg="black",bg="#1887BF").place(x=280, y=330)
                BotonPAFSI = Button(ventana2, text="SI",command=yesfinal,activebackground="blue").place(x=300, y=370)
                BotonPAFNO = Button(ventana2, text="NO",command=nofinal,activebackground="blue").place(x=360, y=370)
        def yesp():           
            if n % 2 == 0:
                etiquetaPares8 = Label(ventana2, text="Correcto.El numero ingresado es par",fg="black",bg="#1887BF").place(x=250, y=310)
                etiquetaPares12 = Label(ventana2, text="Quieres seguir jugando?",fg="black",bg="#1887BF").place(x=280, y=330)
                BotonPAFSI = Button(ventana2, text="SI",command=yesfinal,activebackground="blue").place(x=300, y=370)
                BotonPAFNO = Button(ventana2, text="NO",command=nofinal,activebackground="blue").place(x=360, y=370)
            else : 
                etiquetapares9 = Label(ventana2, text="Incorrecto.El numero ingresado no es par",fg="black",bg="#1887BF").place(x=250, y=310)
                etiquetaPares12 = Label(ventana2, text="Quieres seguir jugando?",fg="black",bg="#1887BF").place(x=280, y=330)
                BotonPAFSI = Button(ventana2, text="SI",command=yesfinal,activebackground="blue").place(x=300, y=370)
                BotonPAFNO = Button(ventana2, text="NO",command=nofinal,activebackground="blue").place(x=360, y=370)
        def pares():
            etiquetaPares6 = Label(ventana2, text="Este numero es par? ",fg="black",bg="#1887BF").place(x=290, y=210)
            etiquetaPares7 = Label(ventana2, text=str(n),fg="black",bg="#1887BF").place(x=330, y=240)
            botonPA2 = Button(ventana2, text= "SI",command=yesp ,activebackground="blue").place(x=300, y=270)
            botnPA3 = Button(ventana2, text="NO",command=nop,activebackground="blue").place(x=360, y=270)
        #Abrir ventana
        ventana2 = Toplevel(ventana)
        ventana.iconify
        #Diseño de la ventana
        ventana2.geometry('700x450')
        ventana2.title("Jugando Pares")
        etiqueta100 = Label(ventana2, text="Pares",bg="#1887BF")
        etiqueta100.pack()  
        ventana2.config (bg="#1887BF")
        #Etiquetas de la ventana
        etiquetaPares1 = Label(ventana2, text=">>>>>>>> PARES <<<<<<<<",fg="black",bg="#1887BF").place(x=265, y=30)
        etiquetaPares2 = Label(ventana2, text=str(N[0])+", Recuerda:",fg="black",bg="#1887BF").place(x=60, y=70)
        etiquetaPares3 = Label(ventana2, text="Un numero es par si se puede ser dividio entre 2",fg="black",bg="#1887BF").place(x=60, y=90)
        etiquetaPares4 = Label(ventana2, text="Coloque Si,si desea seguir.",fg="black",bg="#1887BF").place(x=60, y=110)
        etiquetaPares5 = Label(ventana2, text="Coloque No,si desea acabar.",fg="black",bg="#1887BF").place(x=60, y=130)
        #Botones Pares 
        botonPA1 = Button(ventana2, text="Inicar Juego", command=pares,activebackground="blue").place(x=260, y=170)
    else :
        messagebox.showerror("Mensaje","Debe Registrar un jugado")
        
 
###Diseño de la Interfaz (Ventana 3 (Impares))
#Ventana Impares 
def abrir_ventana3():
    if int(len(N))>=1 :
        n = random.randint(1,100)
        #Definicion Botones Impares :
        def noifinal():
            messagebox.showinfo("Gracias","Gracias por jugar")
            ventana3.destroy()
        def yesifinal():
            messagebox.showinfo("Mensaje","Sigamos CHIQUIMATENANDO, Abra la ventana de nuevo")
            ventana3.destroy()
        def noip():
            if n % 2 == 0:
                etiquetaPares10 = Label(ventana3, text="Correcto.El numero ingresado no es impar",fg="black",bg="#1887BF").place(x=250, y=310)
                BotonIPAFSI = Button(ventana3, text="SI",command=yesifinal,activebackground="blue").place(x=300, y=370)
                BotonIPAFNO = Button(ventana3, text="NO",command=noifinal,activebackground="blue").place(x=360, y=370)
            else:
                etiquetaPares11 = Label(ventana3, text="Incorrecto.El numero ingresado si es impar",fg="black",bg="#1887BF").place(x=250, y=310)
                BotonIPAFSI = Button(ventana3, text="SI",command=yesifinal,activebackground="blue").place(x=300, y=370)
                BotonIPAFNO = Button(ventana3, text="NO",command=noifinal,activebackground="blue").place(x=360, y=370)
        def yesip():
            if n % 2 != 0:
                etiquetaPares8 = Label(ventana3, text="Correcto.El numero ingresado es impar",fg="black",bg="#1887BF").place(x=250, y=310)
                BotonIPAFSI = Button(ventana3, text="SI",command=yesifinal,activebackground="blue").place(x=300, y=370)
                BotonIPAFNO = Button(ventana3, text="NO",command=noifinal,activebackground="blue").place(x=360, y=370)
            else : 
                etiquetapares9 = Label(ventana3, text="Incorrecto.El numero ingresado no es impar",fg="black",bg="#1887BF").place(x=250, y=310)
                BotonIPAFSI = Button(ventana3, text="SI",command=yesifinal,activebackground="blue").place(x=300, y=370)
                BotonIPAFNO = Button(ventana3, text="NO",command=noifinal,activebackground="blue").place(x=360, y=370)
        def impares():
            etiquetaIPares6 = Label(ventana3, text="Este numero es impar? ",fg="black",bg="#1887BF").place(x=290, y=210)
            etiquetaIPares7 = Label(ventana3, text=str(n),fg="black",bg="#1887BF").place(x=330, y=240)
            botonIPA2 = Button(ventana3, text= "SI",command=yesip ,activebackground="blue").place(x=300, y=270)
            botnIPA3 = Button(ventana3, text="NO",command=noip,activebackground="blue").place(x=360, y=270)
        #Abrir ventana
        ventana3 = Toplevel(ventana)
        ventana.iconify
        #Diseño de la Ventana
        ventana3.geometry('700x450')
        ventana3.title("Jugando Impares")
        etiquetaimpares = Label(ventana3, text="Impares",bg="#1887BF")
        etiquetaimpares.pack()
        ventana3.config (bg="#1887BF")
        #Etiquetas de la ventana
        etiquetaIPares1 = Label(ventana3, text=">>>>>>>> IMPARES <<<<<<<<",fg="black",bg="#1887BF").place(x=265, y=30)
        etiquetaIPares2 = Label(ventana3, text=str(N[0])+", Recuerda:",fg="black",bg="#1887BF").place(x=60, y=70)
        etiquetaIPares3 = Label(ventana3, text="Un numero es impar si no puede ser dividio entre 2",fg="black",bg="#1887BF").place(x=60, y=90)
        etiquetaIPares4 = Label(ventana3, text="Coloque Si,si desea seguir.",fg="black",bg="#1887BF").place(x=60, y=110)
        etiquetaIPares5 = Label(ventana3, text="Coloque No,si desea acabar.",fg="black",bg="#1887BF").place(x=60, y=130)
        #Botones Impares 
        botonIPA1 = Button(ventana3, text="Inicar Juego", command=impares,activebackground="blue").place(x=260, y=170)
    else :
        messagebox.showerror("Mensaje","Debe Registrar un jugador")

### Diseño de la Interfaz (Ventana 4 (Primos))
##Ventana Primos
def abrir_ventana4():
    if int(len(N))>=1 :
        a = 0
        n = random.randint(1,100)
        for i in range (1,n+1):
            if (n % i == 0):
                a = a + 1
        #Definiciones
        def noprifinal():
            messagebox.showinfo("Gracias","Gracias por jugar")
            ventana4.destroy()
        def yesprifinal():
            messagebox.showinfo("Mensaje","Sigamos CHIQUIMATENANDO, Abra la ventana de nuevo")
            ventana4.destroy()
        def nopri():
            if(a !=2):
                etiquetaPris10 = Label(ventana4, text="Correcto.El numero no es primo",fg="black",bg="#1887BF").place(x=270, y=310)
                etiquetaPris15 = Label(ventana4, text=str(n)+" Tiene : "+str(a)+" divisores",fg="black",bg="#1887BF").place(x=290, y=330)
                BotonPRAFSI = Button(ventana4, text="SI",command=yesprifinal,activebackground="blue").place(x=300, y=370)
                BotonPRAFNO = Button(ventana4, text="NO",command=noprifinal,activebackground="blue").place(x=360, y=370)
            else :
                etiquetaPris11 = Label(ventana4, text="Incorrecto.El numero si es primo",fg="black",bg="#1887BF").place(x=270, y=310)
                etiquetaPris14 = Label(ventana4, text=str(n)+" Tiene : "+str(a)+" divisores",fg="black",bg="#1887BF").place(x=290, y=330)
                BotonPRAFSI = Button(ventana4, text="SI",command=yesprifinal,activebackground="blue").place(x=300, y=370)
                BotonPRAFNO = Button(ventana4, text="NO",command=noprifinal,activebackground="blue").place(x=360, y=370)
        def yespri():
            if (a == 2):
                etiquetaPris8 = Label(ventana4, text="Correcto. El numero si es primo",fg="black",bg="#1887BF").place(x=270, y=310)
                etiquetaPris12 = Label(ventana4, text=str(n)+" Tiene : "+str(a)+" divisores",fg="black",bg="#1887BF").place(x=290, y=330)
                BotonPRAFSI = Button(ventana4, text="SI",command=yesprifinal,activebackground="blue").place(x=300, y=370)
                BotonPRAFNO = Button(ventana4, text="NO",command=noprifinal,activebackground="blue").place(x=360, y=370)
                #etiquetaPRI(n, "Tiene:",a,"divisiores")
            else :
                etiquetaPris9 = Label(ventana4, text="Incorrecto. No es primo",fg="black",bg="#1887BF").place(x=270, y=310)
                etiquetaPris13 = Label(ventana4, text=str(n)+" Tiene : "+str(a)+" divisores",fg="black",bg="#1887BF").place(x=290, y=330)
                BotonPRAFSI = Button(ventana4, text="SI",command=yesprifinal,activebackground="blue").place(x=300, y=370)
                BotonPRAFNO = Button(ventana4, text="NO",command=noprifinal,activebackground="blue").place(x=360, y=370)
        def primos():
            etiquetaPris6 = Label(ventana4, text="Este numero es primo? ",fg="black",bg="#1887BF").place(x=290, y=210)
            etiquetaPriss7 = Label(ventana4, text=str(n),fg="black",bg="#1887BF").place(x=330, y=240)
            botonPRI2 = Button(ventana4, text= "SI",command=yespri ,activebackground="blue").place(x=300, y=270)
            botonPRI3 = Button(ventana4, text="NO",command=nopri,activebackground="blue").place(x=360, y=270)
        #Abrir ventana
        ventana4 = Toplevel(ventana)
        ventana.iconify
        ##Diseño de la Ventana
        ventana4.geometry('700x450')
        ventana4.title("Jugando Primos")
        etiquetaprimos = Label(ventana4, text="Primos",bg="#1887BF")
        etiquetaprimos.pack()
        ventana4.config (bg="#1887BF")
        #Etiquetas
        etiquetaPris1 = Label(ventana4, text=">>>>>>>> PRIMOS <<<<<<<<",fg="black",bg="#1887BF").place(x=265, y=30)
        etiquetaPris2 = Label(ventana4, text=str(N[0])+", Recuerda:",fg="black",bg="#1887BF").place(x=60, y=70)
        etiquetaPris3 = Label(ventana4, text="Un numero es primo si el numero solo es divisible entre 1 y en el mismo numero.(Solo tiene 2 divisores.)",fg="black",bg="#1887BF").place(x=60, y=90)
        etiquetaPris4 = Label(ventana4, text="Coloque Si,si desea seguir.",fg="black",bg="#1887BF").place(x=60, y=110)
        etiquetaPris5 = Label(ventana4, text="Coloque No,si desea acabar.",fg="black",bg="#1887BF").place(x=60, y=130)
        #BotonPrimos
        botonPRI1 = Button(ventana4, text="Inicar Juego", command=primos,activebackground="blue").place(x=260, y=170)
    else :
        messagebox.showerror("Mensaje","Debe Registrar un jugador")


###Diseño de la Interfaz (Ventana 5 (Multiplicar))
#Ventana tabala de multiplicar
def abrir_ventana5():
    if int(len(N)) >= 1 :
        #Definición de Botones de Multipicar
        MU = []
        def multi() :
            MU.append(mul.get())
            e1 = Label (ventana5, text= str(MU[0])+" X  1  = "+  str(MU[0]),bg="#1887BF" ).place(x=280, y=190)
            a2 = int(MU[0]) * 2
            e2 = Label (ventana5, text= str(MU[0])+" X  2  = "+  str(a2),bg="#1887BF" ).place(x=280, y=210)
            a3 = int(MU[0]) * 3
            e3 = Label (ventana5, text= str(MU[0])+" X  3  = "+  str(a3),bg="#1887BF" ).place(x=280, y=230)
            a4 = int(MU[0]) * 4
            e4 = Label (ventana5, text= str(MU[0])+" X  4  = "+  str(a4),bg="#1887BF" ).place(x=280, y=250)
            a5 = int(MU[0]) * 5
            e5 = Label (ventana5, text= str(MU[0])+" X  5  = "+  str(a5),bg="#1887BF" ).place(x=280, y=270)
            a6 = int(MU[0]) * 6
            e6 = Label (ventana5, text= str(MU[0])+" X  6  = "+  str(a6),bg="#1887BF" ).place(x=280, y=290)
            a7 = int(MU[0]) * 7
            e7 = Label (ventana5, text= str(MU[0])+" X  7  = "+  str(a7),bg="#1887BF" ).place(x=280, y=310)
            a8 = int(MU[0]) * 8
            e8 = Label (ventana5, text= str(MU[0])+" X  8  = "+  str(a8),bg="#1887BF" ).place(x=280, y=330)
            a9=  int(MU[0]) * 9
            e9 = Label (ventana5, text= str(MU[0])+" X  9  = "+  str(a9),bg="#1887BF" ).place(x=280, y=350)
            a10 = int(MU[0]) * 10
            e10 = Label (ventana5, text= str(MU[0])+" X  10  = "+  str(a10),bg="#1887BF" ).place(x=280, y=370)
            a11 = int(MU[0]) * 11
            e11 = Label (ventana5, text= str(MU[0])+" X  11  = "+  str(a11),bg="#1887BF" ).place(x=280, y=390)
            a12 = int(MU[0]) * 12
            e12 = Label (ventana5, text= str(MU[0])+" X  12  = "+  str(a12),bg="#1887BF" ).place(x=280, y=410)
            ttk.Button(ventana5, text='Volver al Menu', command=ventana5.destroy).pack(side=BOTTOM)
        #Abrir ventana
        ventana5 = Toplevel(ventana)
        ventana.iconify 
        ##Diseño de la Ventana
        ventana5.geometry('700x470')
        ventana5.title("Jugando Multiplicar")
        etiquetamultiplicar = Label(ventana5, text="Multiplicar",bg="#1887BF")
        etiquetamultiplicar.pack()
        ventana5.config (bg="#1887BF")
        #Etiqueta
        mul = StringVar()
        etiquetamult3 = Label(ventana5, text=">>>>>>>> MULTIPLICAR <<<<<<<<",fg="black",bg="#1887BF").place(x=250, y=30)
        etiquetamult4 = Label(ventana5, text=str(N[0])+", Recuerda:",fg="black",bg="#1887BF").place(x=60, y=70)
        etiquetamult5 = Label(ventana5, text="Se le mostrara la tabla de multiplicar del 1 al 12 del número que ingrese ",fg="black",bg="#1887BF").place(x=60, y=90)
        etiquetamult6 = Label(ventana5, text="Ingrese número : ",bg="#1887BF").place(x=190, y=125)
        nu = Entry(ventana5, textvariable = mul).place(x=300, y=125)
        #Botones
        BotonMult = Button(ventana5, text="Mostrar tabla",command=multi,activebackground="blue").place(x=280, y=160)
    else : 
        messagebox.showerror("Mensaje","Debe Registrar un jugador")

#Interfaz Botones 
boton1 = Button(ventana, text="Pares",command=abrir_ventana2,activebackground="blue").place(x=70, y=190)
boton2 = Button(ventana, text="Impares",command=abrir_ventana3,activebackground="blue").place(x=185, y=190)
boton3 = Button(ventana, text="Primos", command=abrir_ventana4,activebackground="blue").place(x=70, y=150)
boton4 = Button(ventana, text="Tabla de multiplicar", command=abrir_ventana5,activebackground="blue").place(x=185, y=150)
boton5 = Button(ventana, text="Ingrese su nombre", command=in_name,activebackground="blue").place(x=120, y=70)

ventana.mainloop()
