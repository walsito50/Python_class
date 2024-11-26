
def comando_insertar():
    backend.insertar(titulo_valor.get(),autor_valor.get(),año_valor.get(),isbn_valor.get())
   




from tkinter import *
import backend



def tomar_la_fila_seleccionada(event):
   
    global filaseleccionada
    
    index=list1.curselection()[0]
    
    filaseleccionada=list1.get(index)
    
  
    e1.delete(0,END)
    e1.insert(END,filaseleccionada[1])    
    e2.delete(0,END)
    e2.insert(END,filaseleccionada[2])    
    e3.delete(0,END)
    e3.insert(END,filaseleccionada[3])    
    e4.delete(0,END)
    e4.insert(END,filaseleccionada[4])  
   
    



def comando_borrar():
    backend.borrar(filaseleccionada[0])
    
    list1.delete(0,END)
    list1.insert(END,"Registro Borrado exitosamente!")
    list1.insert(END," ")
    list1.insert(END, "El registro borrado es: ")
    list1.insert(END," ") 
    list1.insert(END,(filaseleccionada))




def comando_actualizar():
    backend.actualizar(filaseleccionada[0],titulo_valor.get(),autor_valor.get(),año_valor.get(),isbn_valor.get())


 

def comando_ver():   
    list1.delete(0,END)  
    for filas in backend.ver():
        list1.insert(END,filas)

def comando_buscar():
    list1.delete(0,END)
    for filas in backend.buscar(titulo_valor.get(),autor_valor.get(),año_valor.get(),isbn_valor.get()):
        list1.insert(END,filas)

def comando_insertar():
    backend.insertar(titulo_valor.get(),autor_valor.get(),año_valor.get(),isbn_valor.get())
    list1.delete(0,END)
    list1.insert(END,"Registro añadido exitosamente!")
    list1.insert(END," ")
    list1.insert(END, "El registro añadido es: ")
    list1.insert(END," ") 
    list1.insert(END,(titulo_valor.get(),autor_valor.get(),año_valor.get(),isbn_valor.get()))




window=Tk()

window.wm_title("Mi Tienda de Libros")

l1=Label(window,text="Titulo") 
l1.grid(row=0,column=0)

l2=Label(window,text="Autor") 
l2.grid(row=0,column=2)

l3=Label(window,text="Año") 
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN") 
l4.grid(row=1,column=2) 

titulo_valor=StringVar()
e1=Entry(window,textvariable=titulo_valor)
e1.grid(row=0,column=1)

autor_valor=StringVar()
e2=Entry(window,textvariable=autor_valor)
e2.grid(row=0,column=3)

año_valor=StringVar()
e3=Entry(window,textvariable=año_valor)
e3.grid(row=1,column=1)

isbn_valor=StringVar()
e4=Entry(window,textvariable=isbn_valor)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',tomar_la_fila_seleccionada)



sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set) 
sb1.configure(command=list1.yview)

b1=Button(window, text="Vista total", width=15, command=comando_ver)
b1.grid(row=2,column=3)

b2=Button(window, text="Busqueda", width=15,command=comando_buscar)
b2.grid(row=3,column=3)

b3=Button(window, text="Añadir entrada", width=15, command=comando_insertar)
b3.grid(row=4,column=3)

b4=Button(window, text="Actualizar entrada", width=15,command=comando_actualizar)
b4.grid(row=5,column=3)

b5=Button(window, text="Borrar entrada", width=15, command=comando_borrar)
b5.grid(row=6,column=3)

b6=Button(window, text="Cerrar", width=15, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()


