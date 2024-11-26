import mysql.connector

#Establecemos la conexion
con = mysql.connector.connect(
user ="PiqUNo8Bgk",
password = "eaS5zJN2YN",
host = "remotemysql.com",
database = "PiqUNo8Bgk"
)

email2='pruebax@hotmail.com'
altura2=222

cursor = con.cursor()

#cursor.execute("SELECT * FROM data WHERE email='"+ email2 + "'")


cursor.execute("SELECT SUM(altura)/count(altura) FROM data")
promedio=cursor.fetchall()
print(promedio)

