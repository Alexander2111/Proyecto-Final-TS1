correcto=False
num = ""
while(not correcto):
    try:
        num = input("Introduce una palabra: ")
        correcto=True
    except ValueError:
        print('Error, introduce un numero entero')
     
