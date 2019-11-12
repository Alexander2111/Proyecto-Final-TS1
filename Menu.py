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
opcion = 0
 
while True :

 
    print("Bienvenidos a Chiquimatiando")
    print ("1. Pares")
    print ("2. Impares ")
    print ("3. Primos ")
    print ("4. Tabla de Multiplicar")
    print ("5. Fin de la aplicacion")
     
    print ("Elige una opcion")
    opcion = int(input("Ingrese una opcion para jugar:"))
 
    
 
    if opcion == 1:
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
                
            if (ds != "no"):
                print("Formato no aceptado. Solo puede ingresar si o no.")
            elif (ds == "no"):
                print("Gracias por jugar pares.")
                break
            


    elif opcion == 2:
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
                
            elif (ds != "no"):
                print("Formato no aceptado. Solo puede ingresar si o no.")
            elif (ds == "no"):
                print("Gracias por jugar impares.")
                break
        





    elif opcion == 3:
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
                
            elif (ds != "no"):
                print("Formato no aceptado. Solo puede ingresar si o no.")
            elif (ds == "no"):
                print("Gracias por jugar primos")
                break
            


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