carro = {
    'Marca': 'Nissan',
	'Modelo': '350z',
	'Precio': '350,000'
}

carro2 = {
    'Marca': 'Honda',
	'Modelo': 'Civic',
	'Precio': '280,000'
}

print(len(carro)) #Permite saber cuantos atributos tiene el diccionario

carro2.pop('Precio') #Elimina el atributo y elemento del diccionario
print(carro2)

del carro['Marca'] #del funciona como pop()
print(carro)

#del carro. Tambien es posible eliminar todo el diccionario 

carro2.clear() #Limpia el diccionario. Sin embargo no lo elimina
print(carro2)

carro['Color'] = 'Gris' #Es posible agregar atributos al diccionario y elementos al atributo
print(carro)

carroCopy = carro.copy() #Copia todo el diccionario en otro diccionario
print("Copia de carro: ",carroCopy)

carro3 = dict(Marca = "Toyota", #dict, crea un diccionario y permite inicializarlo
              Modelo = "Supra",
              Precio = "625,000"
			  )
print(carro3)

carro4 = ("Marca","Modelo","Precio") #Creamo un nuevo diccionario. (atributo1,atributo2...etc)
carro4 = dict.fromkeys(carro4,"Nulo") #dict.fromkeys inicializa los atributos del diccionario
print(carro4) #dentro de los parentesis se envian los parametros(diccionario,str atributos). Se asigna el string a cada atributo

printAtributos = carro4.keys() #keys() obtiene los atributos del diccionario
print("Atributos: ",printAtributos)

carro4.update({"Marca":"Ford", #Update puede agregar nuevos atributos y actualizar elementos ya existentes
               "Modelo":"Mustang 86",
               "Precio":"250,000",
               "Velocidad_max":"310km/h"})
print("Carro4 actualizado: ",carro4)

if "Marca" in carro4: #Usar if para verificar la existencia de un atributo en el diccionario
    print("El diccionario carro4 si tiene  marca")
else:
     print("El diccionario carro4 no tiene  marca")
     
#Anidar diccionarios
carros = { #Crear un diccionario general. Ej. general = {}
    "coche1" :{ #Posteriormente agregar diccionarios. Con el nombre del diccionario entre "".
         'Marca': 'Nissan', #Ej. "diccionario" : {Atributos} 
	     'Modelo': '350z',
	     'Precio': '350,000'
        },
    "coche2" :{
        'Marca': 'Tesla',
	    'Modelo': 'Model S Plaid',
	    'Precio': '2,125,000' 
        }
    }

print(carros["coche2"])