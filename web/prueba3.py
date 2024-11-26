from flask import Flask, render_template, request
import mysql.connector

from enviar_correo import enviacorre
import conexion

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

        filas=conexion.emailrepetido(email2)
        if len(filas)==0:
        
            con = mysql.connector.connect(
            user ="PiqUNo8Bgk",
            password = "eaS5zJN2YN",
            host = "remotemysql.com",
            database = "PiqUNo8Bgk"
            )

            cursor2 = con.cursor()
            query = cursor2.execute("INSERT INTO data (email,altura) VALUES (%s,%s) ",(email2,altura2))
            con.commit()
            con.close()

            con = mysql.connector.connect(
            user ="PiqUNo8Bgk",
            password = "eaS5zJN2YN",
            host = "remotemysql.com",
            database = "PiqUNo8Bgk"
            )

            cursor3 = con.cursor()
            cursor3.execute("SELECT SUM(altura)/count(altura) FROM data")
            promedio=cursor3.fetchall()
            con.close()
            #print(promedio[0][0])
            promedio=round(promedio[0][0],2)
            
            con = mysql.connector.connect(
            user ="PiqUNo8Bgk",
            password = "eaS5zJN2YN",
            host = "remotemysql.com",
            database = "PiqUNo8Bgk"
            )

            cursor4 = con.cursor()
            cursor4.execute("SELECT count(altura) FROM data")
            cantidad=cursor4.fetchall()
            con.close()

            enviacorre(email2,altura2,promedio,cantidad)  

            return render_template("exito.html")
        else: 
            return render_template("index2.html", text="¡Al parecer este correo ya esta registrado!")
        


  


      

if __name__=="__main__":
    app.run(debug=True)

