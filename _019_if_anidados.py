print("Calculadora")
v1=float(input("\nIntroduce el dato 1: "))
v2=float(input("\nIntroduce el dato 2: "))
print("Selecciona la operacion a realizar\n" +
      "1.- Suma\n"+
      "2.- Resta\n" +
      "3.- Multiplicacion\n" + 
      "4.- Division\n")
operacion = int(input(''))

if operacion == 1: #Dependiendo de la seleccion del usuario el programa entra al if seleccionado
    res=v1+v2
    print("Resultado de la suma: ",res)
if operacion == 2: #Una vez dentro de ese if realiza lo que este dentro del mismo
    res=v1-v2
    print("Resultado de la resta: ",res)
if operacion == 3:
    res=v1*v2
    print("Resultado de la multiplicacion: ",res)
if operacion == 4:
    if v2 == 0:
        print("El denominador no puede ser 0")
    else:
        res=v1/v2
        print("Resultado de la division: ",res)
