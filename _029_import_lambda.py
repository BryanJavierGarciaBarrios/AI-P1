import math #importar libreria para poder usar pi

def area(radio):
	resultado = round(math.pi * radio * radio,3)
	print(resultado)

area(2)

area1 = lambda radio: round(math.pi * radio * radio,3) #Usar lambda reduce las lineas de codigo
print(area1(2))
