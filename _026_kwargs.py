carro = {
    "Marca": "Tesla",
    "Modelo" : "Plaid s",
    "Precio" : "2,000,000"
    }

def funcion(marca,modelo,precio): #Los parametros pueden ser atributos de un diccionario
    print("Marca: " +  marca + "\nModelo: " + 
          modelo + "\nPrecio: " + precio)
    
funcion(carro["Marca"],carro["Modelo"],carro["Precio"]) #Se extraen los elementos del diccionario y se envian como args

def funcion2(**kwargs): #**kwargs envia com argumento los atributos y elementos del diccionario
    for y in kwargs:
        print(y + ":" + kwargs[y])
        
print("Utilizando kwargs")
funcion2(**carro)