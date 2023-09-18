#enconding: utf-8
equipos = ["Manchester","Liverpool","WestHam","Chelsea"]
numeros = (3,4,6,2,34,8)
v1=0

for i in "nombre": #El for se realiza con cada caracter de la palabra
    print(i)
    

for i in equipos: #Tambien se puede aplicar en listas o en tuplas
    print(i)


for i in numeros:
    if i == 2:
        continue #Al aplicar continue, brinca ese elemento del for cuando se cumple la condicion
    print(i)
    

for i in equipos:
    if i == "Liverpool": #Al cumplirse la condicion dentro del for, break rompe el ciclo
        break
    print(i)
    
#For in range

for x in range(3,9,2): #En el ciclo for es posible poner (rango), (rango1,rango2), (rango1,rango2,incremento)
    print(x)
else:
    print("Termino el bucle for")
    
for b in range(2):
    for c in range(2):
        v1 +=1
        print(v1)
