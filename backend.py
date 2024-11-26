import sqlite3

def crear():
    conn2= sqlite3.connect("libreria.bd")
    Cur = conn2.cursor()
    Cur.execute("CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, año INTEGER, isbn INTEGER)") 
    conn2.commit()
    conn2.close()

#nota: coloque año y no me dio error sin embargo
#es preferible usar variables sin ñ por ej fecha
 
def insertar(titulo,autor,año,isbn):
    conn2= sqlite3.connect("libreria.bd")
    Cur = conn2.cursor()
    Cur.execute("INSERT INTO libros VALUES (NULL,?,?,?,?) ",(titulo,autor,año,isbn))
    conn2.commit()
    conn2.close()


def ver():
    conn2= sqlite3.connect("libreria.bd")
    Cur = conn2.cursor()
    Cur.execute("SELECT * FROM libros")
    filas=Cur.fetchall()
    conn2.close()
    return filas
'''
crear()

insertar('El mundo de Sofia','Jostein Gaarder',1991,4582313)
print(ver())
'''

# ahora si vamso a ejecutar 

# nos falta una funcion de busqueda

#escribelo asi primero
#def busqueda(titulo,autor,año,isbn): el priblema de 
#escribirlo asi es que si dan uno solo argumento 
#los otros no tendran valor y dara error 
def buscar(titulo="",autor="",año="",isbn=""):
    conn2= sqlite3.connect("libreria.bd")
    Cur = conn2.cursor()
    Cur.execute("SELECT * FROM libros WHERE titulo=? OR autor=? OR año=? OR isbn=? ", (titulo,autor,año,isbn))
    filas=Cur.fetchall()
    conn2.close()
    return filas

#para realizar la prueba vamos a insertar 2 libros 

#insertar('Una breve historia de casi todo','Bill Bryson',2003,78945685)

#insertar('El mundo y sus demonios','Carl Sagan',1995,413212315)

#vamos a hacer la busuqeda 
#print(ver())
#print(buscar(autor="Jostein Gaarder"))

def borrar(id):
    conn2= sqlite3.connect("libreria.bd")
    Cur = conn2.cursor()
    Cur.execute("DELETE FROM libros WHERE id=? ", (id,))
    conn2.commit()
    conn2.close()

#insertar('Te me vas','Wilmer y Kelvin',2021,87897987)
#print(ver())
#borrar(3)
#print(ver())




def actualizar(id, titulo, autor, año, isbn):
    conn2= sqlite3.connect("libreria.bd")
    Cur = conn2.cursor()
    Cur.execute("UPDATE libros SET titulo=?, autor=?, año=?,isbn=? WHERE id=? ", (titulo, autor, año,isbn,id))
    conn2.commit()
    conn2.close()


#insertar('Te me vas','Wilmer y Kelvin',2021,87897987)
#print(ver())
#actualizar(3,'Programming Python','Wilmer y Kelvin',2021,87897987)
#print(ver())