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
        print("Opcion 3")
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