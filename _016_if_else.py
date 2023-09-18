from traceback import print_tb


label1="Hola"
label2="Como estas"

if label1==label2: #El operador '==' pregunta si los dos elementos son iguales
    print("Las etiquetas son iguales") #Si devuelve un true, entonces realiza las operaciones dentro del if
else:
    print("Las etiquetas no son iguales") #Si la sentencia es false, salta las primeras instrucciones 
    #Y realiza el segundo bloque de instrucciones
    
if label1!=label2:
    print("Las etiquetas no son iguales Utilizando el operador !=")
else:
    print("Las etiquetas son iguales. ")