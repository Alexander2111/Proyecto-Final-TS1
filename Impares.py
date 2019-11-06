import os,sys
import random
os.system("cls")


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
    
    while True:
        ds = input("¿Desea seguir?:").lower()
        if (ds == "si") :
            print("Continue.")
            break
        elif (ds != "no"):
            print("Formato no aceptado. Solo puede ingresar si o no.")
        elif (ds == "no"):
            print("Gracias por jugar impares.")
            sys.exit()
            
    








