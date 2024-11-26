from flask import Flask, render_template, request
import mysql.connector

from enviar_correo import enviacorre

#Establecemos la conexion
con = mysql.connector.connect(
user ="PiqUNo8Bgk",
password = "eaS5zJN2YN",
host = "remotemysql.com",
database = "PiqUNo8Bgk"
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/exito',methods=['POST'])
def exito():
    if request.method=='POST':
        email2=request.form["varemail"]
        altura2=request.form["varaltura"]        
           
        
        # para chequera si la base de datos 
        # ya tiene ese correo 
        cursor = con.cursor()
        cursor.execute("SELECT * FROM data WHERE email='"+ email2 + "'")
        filas=cursor.fetchall()

        if len(filas)==0:
            cursor2 = con.cursor()
            query = cursor2.execute("INSERT INTO data (email,altura) VALUES (%s,%s) ",(email2,altura2))
            con.commit()

            cursor3 = con.cursor()
            cursor3.execute("SELECT SUM(altura)/count(altura) FROM data")
            promedio=cursor3.fetchall()
            #vamos a tomar dos decimales de aproximacion 
            promedio=round(promedio,2)
            print(promedio)

            #vamos a calcular tambien la cantidad
            cursor4 = con.cursor()
            cursor4.execute("SELECT count(altura) FROM data")
            cantidad=cursor3.fetchall()
            
            enviacorre(email2,altura2,promedio,cantidad)  
            
            return render_template("exito.html")
        else: 
            return render_template("index2.html", text="¡Al parecer este correo ya esta registrado!")
        


        '''
sql ="INSERT INTO diccionario(Expresion, Definicion) VALUES ('%s' , '%s')" %(data.keys() , data.values())

        cursor.execute("SELECT email FROM data WHERE email='%s'" %(email2))
        filas=cursor.fetchall()
        print(filas)
        return render_template("exito.html")
'''


'''
        #el codigo para insertar en la tabla 
        cursor = con.cursor()
        query = cursor.execute("INSERT INTO data (email,altura) VALUES (%s,%s) ",(email2,altura2))
        con.commit()
'''
            

if __name__=="__main__":
    app.run(debug=True)

