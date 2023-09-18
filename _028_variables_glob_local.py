i=3 #Con variables globales, y se pueden utilizar desde cualquier lugar. Si se utliza dentro de una funcion, se considera local
j=4

def suma(): #en este caso las variables son locales y no pueden ser accedidas desde fuera
    x=2
    y=9
    print("Resultado: ",x+y)
    
suma()

def resta():
    x=2
    # Agregar global antes de la variable para poder acceder desde fuera de la funcion
    global b 
    b = 9
    print("Resultado: ",x-b)
    def multiplicacion():
        print("Multiplicacion: ",x*b) #Como la segunda funcion multiplicacion esta anidad, puede usar variables locales
    multiplicacion()
    
resta()

