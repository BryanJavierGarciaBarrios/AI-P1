class arma(): #Se crea la clase y se definen los atributos de la clase
   tipo = "SMG"
   camo = "Defecto"
   cargador = 45
   recarga = False
   evolucion = False
   
   def info(self): #Se estalecen los metodos de la clase
      print("Categoria: ", self.tipo, 
            "\nCamo: ", self.camo,"Cargador: ",self.cargador)
      
   def rel(self):
      if (self.cargador<45 and self.recarga):
            self.cargador=45
            print("Arma recargada")
      else:
          print("Arma con balas")
            
   def evo(self):
       if (self.evolucion == True):
           self.camo = "Nivel 2"
           print("Arma evolucionada")
       else:
          print("Arma no evolucionada") 
          
mp5 = arma()
mp5.info()
mp5.rel()
mp5.evo()

print("\nClase persona con __init__")
class persona():
    
    nombre=""
    edad=""
    
    def __init__(self,nombre,edad): #Constructor de la clase. Pide estos datos al crear un objeto
        self.nombre=nombre
        self.edad=edad
        
    def saludar(self):
        print("Hola me llamo ",self.nombre,"tengo ",self.edad)
        
persona1 = persona("Pablo",28) #Los argumentos son necesarios para inicializar el objeto
persona1.saludar()

#Cambiar atributos de un objeto
print("\nCambiando un atributo del objeto")
persona1.nombre = "Juan"
persona1.saludar()

#Nota
#Para eliminar atributos de un objeto usar: del objeto.atributo
#Para eliminar un objeto utilizar del objeto

class estudiante(persona):
    grado=""
    grupo=""
    def __init__(self,nombre,edad,grado,grupo):
        persona.__init__(self,nombre,edad)
        self.grado=grado
        self.grupo=grupo
        
    def estu_saludar(self):
        print("Hola me llamo ",self.nombre,"tengo ",self.edad,"estudio el ",self.grado,"en el grupo ",self.grupo)
        
estudiante1 = estudiante("Ana","21","6","E")
print("\nEstudiante heredando de la clase persona")
estudiante1.estu_saludar()