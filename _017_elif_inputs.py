temperatura=float(input("Ingrese su temperatura corporal: "))

#elif funciona como un if anidado, es decir, si no se cumple la condicion pregunta por elif
if temperatura >= 36 and temperatura<=37.5: 
    print("Temperatura dentro de rango saludable")
    
elif temperatura >37.5: 
    print("Temperatura por encima del rango saludable")
   
elif temperatura <36:
    print("Temperatura por debajo del rango saludable")
