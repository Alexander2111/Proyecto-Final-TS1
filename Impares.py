import os
import random
os.system("cls")

print("Recuerde:")
print("Un numero es impar si no puede ser dividio entre 2.")
print("Coloque Si,si desea seguir.")
print("Coloque No,si desea acabar.")


while True:
    n = random.randint(1,100)
    p = input("¿El numero "+ str(n) +" es impar?:").lower()
    if n % 2 != 0:
        if (p == "si"):
            print("Correcto.El numero ingresado es impar")
        if(p == "no"):
            print("Incorrecto.El numero ingrsado no es impar.")
    if (n % 2 == 0):
        if (p == "si"):
            print("Incorrecto.El numero ingresado no es impar")
        if(p == "no"):
            print("Correcto.El numero ingrsado es impar.")
    
        
    ds = input("¿Desea seguir?:").lower()
    if (ds == "no"):
        break








