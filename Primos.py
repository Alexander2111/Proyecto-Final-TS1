import os
os.system("cls")
print("Recuerde:")
print("Un numero es primo si el numero solo es divisible entre 1 y en el mismo numero.")
a = 0
while True:
    n = int(input("Ingrese numero primo:"))
    for i in range (1,n+1):
        if (n % i == 0):
            a = a + 1
    if(a !=2):
        print("Incorrecto. No es primo.")
    if (a==2):
        print("Correcto. Si es primo.")
    ds = input("¿Desea seguir?:").lower()
    if (ds == "no"):
        break
print("Juego Finalizado.") 		