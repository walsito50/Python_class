import mysql.connector

from enviar_correo import enviacorre


#Establecemos la conexion
con = mysql.connector.connect(
user ="PiqUNo8Bgk",
password = "eaS5zJN2YN",
host = "remotemysql.com",
database = "PiqUNo8Bgk"
)


cursor = con.cursor()
email2='wlopez18@hotmail.com'
altura2=555
id2=25
'''
query = cursor.execute("INSERT INTO data (email,altura) VALUES (?,?) ",(email2,altura2))
cursor.execute("INSERT INTO data (email,altura) VALUES (%s,%s) ",(email2,altura2))
'''

cursor = con.cursor()
cursor.execute("SELECT * FROM data WHERE email='"+ email2 + "'")

#consulta="SELECT * FROM data WHERE email='"+ email2 + "'"
#consulta="INSERT INTO data (email,altura) VALUES (%s,%s) ",(email2,altura2)
filas=cursor.fetchall()
if len(filas)>0:
    print("si son iguales")
else:
    print("no son iguales")

#print(query)
#con.commit()


#probando lo de enviar correo 
#enviacorre(email2,altura2)