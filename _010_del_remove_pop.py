carros=["tesla","audi","toyota","nissan","mercedes","ford"]
print("Array original: ",carros)
del carros[0] #Para elimiar elementos de una lista basta con escribir del(lista[pos])
print(carros)
carros=["tesla","audi","toyota","nissan","mercedes","ford"]
del(carros[-1]) #Tambien es posible eliminar con la posicion negativa
print(carros)

carros=["tesla","audi","toyota","nissan","mercedes","ford"]
carros.remove("mercedes") #Otra forma de eliminar un elemento es con su nombre
print(carros)

carros=["tesla","audi","toyota","nissan","mercedes","ford"]
guardarDato=carros.pop(2) #El metodo pop permite almacenar el dato eliminado en otra variable
print(carros)
print("\nEl elemento eliminado es: " + guardarDato)
