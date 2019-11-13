import os
import random
os.system("cls")
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False



# Entrada:ingresar la edad

print("Hola. Solo puedes jugar si tienes la edad de 8 a 13.")
while True:

    try:
        while True:
            edad = int(input("Ingrese su edad por favor:"))
            if 7<edad <14:
                break
            else:
              print("Lo siento. No cuenta con la edad para poder jugar.")

        
        break
    except ValueError:
        print("Formato no aceptado.Intentelo de nuevo")

nombre = input("Ingrese nombre por favor: ")
print("Hola ",nombre)




# Entrando al juego 

opcion = 0
while True :

 
    print("*******Bienvenidos a Chiquimatiando*********")
    print("Las opciones a jugar son las siguientes:")
    print ("1. Pares")
    print ("2. Impares ")
    print ("3. Primos ")
    print ("4. Tabla de Multiplicar")
    print("Para salir coloque la siguiente opcion:")
    print ("5. Fin de la aplicacion")
    print("")
    while True:

        try:
            while True:
                opcion = int(input("Ingrese una opcion para jugar:"))
                if 0<opcion<6:
                    break
                else:
                    print("Lo siento. Solo puede ingresar opciones del 1 al 5.")

            
            break
        except ValueError:
            print("Formato no aceptado.Intentelo de nuevo")
    
 
    
# Pares 

    if opcion == 1:
        print("")
        print("*****JUGANDO PARES******")
        print("Recuerde:")
        print("Un numero es par si se puede ser dividio entre 2.")
        print("Coloque Si,si desea seguir.")
        print("Coloque No,si desea acabar.")
        while True:
            n = random.randint(1,100)    
            while True:
                p = input("¿El numero "+ str(n) +" es par?:").lower()
                if n % 2 == 0:
                    if (p == "si"):
                        print("Correcto.El numero ingresado es par")
                        break
                    elif(p == "no"):
                        print("Incorrecto.El numero ingresado si es par.")
                        break
                    else:
                        print("Formato no aceptado. Solo puede ingresar si o no.")

                elif (n % 2 != 0):
                    if (p == "si"):
                        print("Incorrecto.El numero ingresado no es par")
                        break
                    elif(p == "no"):
                        print("Correcto.El numero ingresado no es par.")
                        break
                    else:
                        print("Formato no aceptado. Solo puede ingresar si o no.")
            
            
            ds = input("¿Desea seguir?:").lower()
            if (ds == "si") :
                print("Continue.")
            
            elif (ds == "no"):
                print("Gracias por jugar pares.")
                print("")
                break
            con = ""
            while (ds != "no"and ds!="si") :
                print("Formato no aceptado. Solo puede ingresar si o no.")
                print("Por favor intentelo de nuevo")
                print("")
                con = input("¿Desea seguir?:").lower()
                
                if con == "si" or con =="no":
                    break
            if (con == "si") :
                print("Continue.")
            
            elif (con == "no"):
                print("Gracias por jugar pares.")
                print("")
                break
          
            

# Impares

    elif opcion == 2:
        print("")
        print("*****JUGANDO IMPARES*****")
        print("Recuerde:")
        print("Un numero es impar si no puede ser dividio entre 2.")
        print("Coloque Si,si desea seguir.")
        print("Coloque No,si desea acabar.")
        while True:
            n = random.randint(1,100)

            while True:
                p = input("¿El numero "+ str(n) +" es impar?:").lower()
                if n % 2 != 0:
                    if (p == "si"):
                        print("Correcto.El numero ingresado es impar")
                        break
                    elif(p == "no"):
                        print("Incorrecto.El numero ingresado si es impar.")
                        break
                    else:
                        print("Formato no aceptado. Solo puede ingresar si o no.")
            
                elif (n % 2 == 0):
                    if (p == "si"):
                        print("Incorrecto.El numero ingresado no es impar")
                        break
                    elif(p == "no"):
                        print("Correcto.El numero ingresado no es impar.")
                        break
                    else:
                        print("Formato no aceptado. Solo puede ingresar si o no.")
            
            
            ds = input("¿Desea seguir?:").lower()
            if (ds == "si") :
                print("Continue.")
            
            elif (ds == "no"):
                print("Gracias por jugar impares.")
                print("")
                break
            con = ""
            while (ds != "no"and ds!="si") :
                print("Formato no aceptado. Solo puede ingresar si o no.")
                print("Por favor intentelo de nuevo")
                print("")
                con = input("¿Desea seguir?:").lower()
                
                if con == "si" or con =="no":
                    break
            if (con == "si") :
                print("Continue.")
            
            elif (con == "no"):
                print("Gracias por jugar impares.")
                print("")
                break
        




# Primos

    elif opcion == 3:
        print("")
        print("*****JUGANDO PRIMOS*****")
        print("Recuerde:")
        print("Un numero es primo si el numero solo es divisible entre 1 y en el mismo numero.(Solo tiene 2 divisores.)")
        print("Coloque Si , si desea seguir. ")
        print("Coloque No , si desea finalizar. ")

        a = 0
        while True:

            n = random.randint(2,100)
            while True:
                p = input("¿El numero "+ str(n) +" es primo?:").lower()
                for i in range (1,n+1):
                    if (n % i == 0):
                        a = a + 1
            
    
                if(a !=2):
                    if (p == "si"):
                        print("Incorrecto. No es primo.")
                        print(n, "Tiene:",a,"divisiores")
                        a = a -a
                        break
                    elif (p == "no"):
                        print("Correcto.El numero no es primo")
                        print(n, "Tiene:",a,"divisiores")
                        a = a -a
                        break
                    else:
                        print("Formato no aceptado. Solo puede ingresar si o no.")
                if (a == 2):
                    if (p == "si"):
                        print("Correcto. El numero si es primo.")
                        print(n, "Tiene:",a,"divisiores")
                        a = a -a
                        break
                    elif (p == "no"):
                        print("Incorrecto.El numero si es primo")
                        print(n, "Tiene:",a,"divisiores")
                        a = a -a
                        break
                    else:
                        print("Formato no aceptado. Solo puede ingresar si o no.")
        
            

    
            
            ds = input("¿Desea seguir?:").lower()
            if (ds == "si") :
                print("Continue.")
            
            elif (ds == "no"):
                print("Gracias por jugar primos.")
                print("")
                break
            con = ""
            while (ds != "no"and ds!="si") :
                print("Formato no aceptado. Solo puede ingresar si o no.")
                print("Por favor intentelo de nuevo")
                print("")
                con = input("¿Desea seguir?:").lower()
                
                if con == "si" or con =="no":
                    break
            if (con == "si") :
                print("Continue.")
            
            elif (con == "no"):
                print("Gracias por jugar primos.")
                print("")
                break
            

# Tablas de multiplicar

    elif opcion == 4:
        x = int(input("Ingrese que tabla desea aprender"))
        rango=range(1,13)
        for elemento in rango:
            producto = x*elemento
            print(x," x ",elemento," = ",producto)
           
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")
 
print ("Fin")