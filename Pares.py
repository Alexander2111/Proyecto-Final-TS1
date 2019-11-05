import os
import random
os.system("cls")

print("Recuerde:")
print("Un numero es par si se puede ser dividio entre 2.")
print("Coloque Si,si desea seguir.")
print("Coloque No,si desea acabar.")


while True:
    n = random.randint(1,100)
    p = input("¿El numero "+ str(n) +" es par?:").lower()

    if n % 2 == 0:
        if (p == "si"):
            print("Correcto.El numero ingresado es par")
        elif(p == "no"):
            print("Incorrecto.El numero ingresado si es par.")
        else:
            print("Formato no aceptado")
            
    if (n % 2 != 0):
        if (p == "si"):
            print("Incorrecto.El numero ingresado no es par")
        elif(p == "no"):
            print("Correcto.El numero ingresado no es par.")
        else:
            print("Formato no aceptado")
    
    ds = input("¿Desea seguir?:").lower()
    if (ds == "no"):
        break
