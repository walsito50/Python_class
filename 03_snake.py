import turtle
import time
import random

posponer = 0.1

#Marcadores de score
score=0
highscore=0

# configuracion de la pantalla
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width= 600, height=600)
wn.tracer(0)

#Cabeza de serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
cabeza.color("white")

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")

# Cuerpo de la serpiente 
cuerposerpiente=[]


# texto 
texto =turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(5,260)
texto.write("Score: 0     High Score: 0", align="center", font=("Courier", 24, "normal"))

#Funciones
def arriba():
    cabeza.direction ="up"
def abajo():
    cabeza.direction ="down"
def derecha():
    cabeza.direction ="right"
def izquierda():
    cabeza.direction ="left"


def mov():
    if cabeza.direction =="up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction =="down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direction =="left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction =="right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
#Teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(derecha,"Right")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(abajo,"Down")


#esto desde le principio para que se pueda quedar visible al ventana 
while True:
    wn.update()
    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor()< -280 or cabeza.ycor()> 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        for nuevocuerposer in cuerposerpiente:
            nuevocuerposer.goto(1000,1000)

        cuerposerpiente.clear()
        #Limpiar lista de segmentos

        # Resetear marcador 
        score = 0
        texto.clear()
        texto.write("Score: {}     High Score: {}".format(score,highscore), align="center", font=("Courier", 24, "normal"))

    #importamos el modulo random 
    if cabeza.distance(comida)<20:
        x=random.randint(-280, 280)
        y=random.randint(-280, 280)
        comida.goto(x,y)

        #para seleccionar todas las palabras que quieres cambiar 
        #control d y luego escribes el nombre nuevo
        nuevocuerposer = turtle.Turtle()
        nuevocuerposer.speed(0)
        nuevocuerposer.shape("square")
        nuevocuerposer.penup()
        nuevocuerposer.color("grey")
 #por defecto se crea el cuadrado en el centro de mi 
        cuerposerpiente.append(nuevocuerposer)

        #aumentar marcador 
        score =score + 10
        if score > highscore:
            highscore = score 
        texto.clear()
        texto.write("Score: {}     High Score: {}".format(score,highscore), align="center", font=("Courier", 24, "normal"))
    #ahora vamso a mover el cuerpo 
    totalcuerpo = len(cuerposerpiente)
    for i in range(totalcuerpo-1,0,-1):
        x= cuerposerpiente[i -1].xcor()
        y= cuerposerpiente[i -1].ycor()
        cuerposerpiente[i].goto(x,y)

    if totalcuerpo>0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        cuerposerpiente[0].goto(x,y)


    mov()
    #Colisiones con el cuerpo
    for nuevocuerposer in cuerposerpiente:
        if nuevocuerposer.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction= "stop"

            #Esconder os segmentos
            for nuevocuerposer in cuerposerpiente:
                nuevocuerposer.goto(1000,1000)
            cuerposerpiente.clear()
            # Resetear marcador 
            score = 0
            texto.clear()
            texto.write("Score: {}     High Score: {}".format(score,highscore), align="center", font=("Courier", 24, "normal"))


    time.sleep(posponer)
