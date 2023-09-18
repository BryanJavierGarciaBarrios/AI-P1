def hola(): #Para definir una funcion se utiliza def nombreFuncion()
	print("Hola mundo") 

hola() #Llama a la funcion y ejecuta lo que este dentro de la misma

dat1 = float(input("Ingresa el dato 1: "))
dat2 = float(input("Ingresa el dato 2: "))

def suma(val1,val2): #Los argumentos deben ser separados por una coma
	res=val1+val2
	print("Resultado de la suma:",res)
	
suma(dat1,dat2) #Al llamar la funcion debemos asignar los argumentos de la funcion
