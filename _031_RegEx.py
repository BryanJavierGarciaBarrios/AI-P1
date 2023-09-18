import re

frase = "Yo solo se que no se nada. Socrates"

buscar = re.search("se",frase) #re.search("",str) Permie buscar caracteres dentro de un string
#Y devuelve la posicion en la que se encuentran dentro de este
#Despues de encontrar una coincidencia, se detiene
print(buscar)

buscarTodo = re.findall("o",frase) #re.findall("",str). Encuentra todas la coincidencias en un str
print(buscarTodo) #Si no encuentra nada el resultado es []

res = re.split("s",frase) #Split separa de un str el argumento de busqueda
#Es decir si el argumento es un espacio " " retornara el str sin los espacios
print(res)

resultado = re.sub(" ","_",frase) #re.sub() sustituye los parametro de busqueda
#Por el parametro especificado en un determinado str
print(resultado)

res1 = re.findall("se|nada|Yo",frase) #Metacaracteres | permite buscar un resultado u otro
print(res1)

res1 = re.findall("So..a..s",frase) #Sustituye los puntos por coincidencias
print(res1)

res1 = re.findall("[a-d]",frase) #Encuentra caracteres del str en ese rango especifico
print(res1)