#El diccionario permite asociar atributos a una sola variable (como una clase)
carro = { #Diccionario{atributo1, atributo2,...,atributoN}
	'Marca': 'Honda',
    'Modelo': '2020',
	'Precio': '450,000mxn',
}

consulta = carro['Modelo'] #Es posible consultar un sol atributo del diccionario
print("Modelo" + consulta)
print(carro) #O consultar todo el diccionario

mostrar = dict(carro) #Tambien muestra todo el diccionario
print(mostrar)

#Otra forma de acceder a un elemento es con get()
print("Precio: " + carro.get("Precio"))

#Uso de ciclo for con diccionarios
print("\nAtributos del carro: ")
for x in carro:
    print(x) #En este caso el ciclo for obtiene los atributos, pero no los valores de estos
    
print("Elementos de los atributos del carro: ")
for x in carro:
    print(carro[x]) #En este caso el ciclo for obtiene los elementos (valores) de los atributos
    
print("Elementos de los atributos del carro con values()")
for x in carro.values(): #Values retorna los valores de los atributos
    print(x) 
    
print("Elementos y atributos con items()")
for x,y in carro.items(): #En el ciclo for se determina x,y. x=posicion del atributo. y=Elemento(valor) del atributo
    print(x,"=",y) #Imprime las variables x y y (atributos '=' elementos)


