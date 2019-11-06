import os,sys
import random
os.system("cls")

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

    while True:
        ds = input("¿Desea seguir?:").lower()
        if (ds == "si") :
            print("Continue.")
            break
        elif (ds != "no"):
            print("Formato no aceptado. Solo puede ingresar si o no.")
        elif (ds == "no"):
            print("Gracias por jugar pares.")
            sys.exit()



