import mysql.connector

def emailrepetido(email2):
    con = mysql.connector.connect(
    user ="PiqUNo8Bgk",
    password = "eaS5zJN2YN",
    host = "remotemysql.com",
    database = "PiqUNo8Bgk"
    )

    cursor = con.cursor()
    cursor.execute("SELECT * FROM data WHERE email='"+ email2 + "'")
    filas=cursor.fetchall()
    con.close()
    return filas
