import time

nombre= input("Por favor ingrese su nombre: ")
print(" Hola ", nombre, "Es hora de jugar al ahorcado")

print(" ")
time.sleep(1)
print("comienza a adivinar ")
time.sleep(0.5)


palabra="python"

tupalabra=""
vidas=5

while vidas>0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas +=1

    if fallas==0:
        print(" ")
        print("Waoooo eres un pro")
        break

    print(" ")
    tuletra=input("Introduzca una letra: ")
    tupalabra +=tuletra

    if tuletra not in palabra:
        vidas -=1
        print("Upppps te equivocastes")
        print(" Tu tienes %i vidas" %(vidas))

    if vidas==0:
        print("Lo siento estas ahorcado")
else:
    print("Gracias por participar")