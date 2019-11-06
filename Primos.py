import os,sys
import random
os.system("cls")
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
    
        

   
    while True:
        ds = input("¿Desea seguir?:").lower()
        if (ds == "si") :
            print("Continue.")
            break
        elif (ds != "no"):
            print("Formato no aceptado. Solo puede ingresar si o no.")
        elif (ds == "no"):
            print("Gracias por jugar primos")
            sys.exit()
   