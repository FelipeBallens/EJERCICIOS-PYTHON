import random

print("EJERCICIO 2. NUMEROS ALEATORIOS EN UN RANGO: \n") ## descripcion
# SOLICITA INFORMACION AL USUARIO
maximo = input("Digite el Maximo del rango: ")
minimo = input("Digite el Minimo del rango: ")
numeros = input("Digite cuantos numeros aleatorios: ")
Aleatorios = []
# CONVIERTE NUMEROS A ENTEROS
Maximo = int(maximo)
Minimo = int(minimo)
Numeros = int(numeros)
# SE GENERAN LOS NUMEROS ALEATORIOS
for i in range(0,Numeros):
    b = random.randint(Minimo,Maximo)
    Aleatorios.append(b)
    
print("Numeros aleatorios: ",Aleatorios)
    
