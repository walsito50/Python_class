from flask import Flask, render_template, request
import mysql.connector

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
        print(email2, altura2) 
            
        #el codigo para insertar en la tabla 
    
        cursor = con.cursor()
        query = cursor.execute("INSERT INTO data (email,altura) VALUES (%s,%s) ",(email2,altura2))
        con.commit()

        return render_template("exito.html")    

if __name__=="__main__":
    app.run(debug=True)

