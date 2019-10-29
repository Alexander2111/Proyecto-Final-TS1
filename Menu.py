import os
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
 
while not salir:
 
    print ("1. Pares")
    print ("2. Impares ")
    print ("3. Primos ")
    print ("4. Tabla de Multiplicar")
    print ("5. Fin de la aplicacion")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opcion 1")
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
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
        print("Eliga nueva opcion") 		
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