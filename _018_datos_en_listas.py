marcas=["Apple","Samsung","Huawei","Xiaomi"]
tupla1=("Apple","Samsung","Huawei","Xiaomi")
entrada=input("Ingrese el nombre de una marca de celulares: ")

if entrada in marcas: #El operador in, pregunta si la entrada existe en la lista y retorna true o false
    print("La marca esta en la lista")
else:
   print("La marca no esta en la lista") 
   
#Ahora con una tupla 
entrada2=input("Ingrese el nombre de una marca de celulares: ")  
if entrada2 in tupla1: #El operador in, pregunta si la entrada existe en la lista y retorna true o false
    print("La marca esta en la lista")
else:
   print("La marca no esta en la lista")