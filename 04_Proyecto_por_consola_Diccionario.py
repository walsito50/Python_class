
import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def midiccionario(palabra):
    palabra = palabra.lower()
    if palabra in data:
        return data[palabra]
    elif len(get_close_matches(palabra,data.keys()))>0:
        respuesta = input("Quizas esta buscando %s ?. Presione S en caso de si o N en caso de No: " % get_close_matches(palabra,data.keys(),1)[0])
        if respuesta == "S":
            return data[get_close_matches(palabra,data.keys())[0]]
        elif respuesta =="N":
            return "La palabra no existe, muy buenos dias"
        else: 
            return "Lo sentimos mucho, pero no entendemos su respuesta"
    else:
        return "La palabra no existe, Por favor verifique su entrada. "

lapalabra= input("Por favor ingrese la palabra que desea buscar en el diccionario: ")

salida = midiccionario(lapalabra) #salida seria una lista 
if type(salida) == list:
    for elementos in salida:
        print(elementos)
else:
    print(salida)
