import random


opciones=["Piedra", "Papel", "Tijera"]

#el turno de la maquina
magia =random.randint(0,2) #aleatorio 0= piedra 1=pape....
compu = opciones[magia]

#print(magia)
print(" Eleccion de la computadora: ",compu)

#con el turno del humano
tu =input("Dame tu opción: ")
print("Tu selección fue: ", tu)

if (tu==compu):
    print("Empatados!")

if (tu=="Tijera"):
    if (compu=="Papel"):
        print("Ganastes! yeahhh")
    if (compu=="Piedra"):
        print("Perdistes! :(")

if (tu=="Papel"):
    if (compu=="Piedra"):
        print("Ganastes! yeahhh")
    if (compu=="Tijera"):
        print("Perdistes! :(")

if (tu=="Piedra"):
    if (compu=="Tijera"):
        print("Ganastes! yeahhh")
    if (compu=="Papel"):
        print("Perdistes! :(")