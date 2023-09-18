#Ciclo while
x = 1
y = 10
z = 10

while x <= 10: #El ciclo ejecuta una accion en bucle hasta que se cumpla la condicion
	print(x)
	x += 1
else: #El else permite ejecutar una accion una vez hayas salido del bucle
	print("Saliste del while 1\n") 
	
while y >= 0: #El ciclo ejecuta una accion en bucle hasta que se cumpla la condicion
	print(y)
	if y ==5: #Al poner un if anidado al cumplirse la condicion del if
		break #El break saca del while
	y -= 1
	
print("\n")	
while z > 0: #El ciclo ejecuta una accion en bucle hasta que se cumpla la condicion
	z -= 1
	if z ==3 or z==8: #Al poner un if anidado al cumplirse la condicion del if
		continue #"continue" permite que el ciclo se siga ejecutando saltandose la condicion del if
	print(z) #El printe debe ir despues del continue
	
	

