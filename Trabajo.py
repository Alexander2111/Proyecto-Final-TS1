import random

print("Bienvenido a Chiquimateando")
name = input("Hola,Cual es tu nombre : ")
print("Hola",name) 
edad = int(input("Cual es tu edad ? : "))

if 7 > edad :
    print("Lo sentimos eres muy pequeño para poder practicar los temas ")
if 13 < edad : 
    print("Este juego ya no esta a tu nivel busca otra manera de practicar")

x = int(input("Hasta que número dominas : "))
print("Esta bien",name,"procede a elejir un tema que quieras practicar")
numeros = range(1,x)
randomnumeros = random.randint(0,x)
print("Que quieres practicar : pares/impares/primos/tabla de multiplicar")
respuesta = input ("")
if  respuesta  == "pares" :
    print("Estas jugando aprender pares")    
if respuesta == "impares":
    print("Estas jugando aprender impares")
if respuesta == "primos":
    print("Estas jugando aprender impares")
if respuesta == "tabla de multiplicar":
    print("Estas jugando aprender tabla de multiplicar")

















