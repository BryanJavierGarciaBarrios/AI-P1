try: #try-catch, permite ejecutar el codigo y detectar errores
    print(variable)
except:
    print("Algo salio mal")
    
try: #ejemplo de codigo sin error
    x="Aqui si se define la variable"
    print(x)
except:
    print("variable no encontrada")
