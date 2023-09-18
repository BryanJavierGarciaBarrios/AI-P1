# -*- encoding: utf-8 -*-

def marcas(*args): #*args hace referencia a una lista de datos, por lo que es un argumento variable en tamaño
    print(args)

def juegos(company,studio,*juegos): #Agregar dos argumentos y un *args
    print("Empresa: " + company + "\nEstudio: " + studio)
    for y in juegos: #Aqui solo se llama al nombre de la lista
        print("Juego: " + y)

carros = ["Lamborgini","Mercedes","Honda","Toyota"]
marcas(*carros) #Lamar a la funcion con *lista 0 *tupla        
codTrey = ["Black Ops 1","Blac Ops 2", "Black Ops 3","Blac Ops 4","Black Ops: Cold war"]
juegos("Activision","Treyarch",*codTrey) #Se llama a la funcion y se envian los argumentos