import numpy as np
## descripcion
# 1. Operaciones con vectores

# Definir los vectores
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

print("Vector 1:", vector1)
print("Vector 2:", vector2)

# Sumar los vectores
resultado1 = vector1 + vector2

print("El resultado de la suma es:", resultado1)

# Restar los vectores
resultado2 = vector1 - vector2

print("El resultado de la resta es:", resultado2)

# Producto punto de los vectores
producto_punto = np.dot(vector1, vector2)

print("El producto punto es:", producto_punto)

# Producto cruz de los vectores
producto_cruz = np.cross(vector1, vector2)

print("El producto cruz es:", producto_cruz)

# Dividir elemento por elemento
division_elemento_por_elemento = vector1 / vector2

print("La división elemento por elemento es:", division_elemento_por_elemento,"\n")

#2 Operaciones con matrices

matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

print("Matriz 1:\n", matriz1)
print("Matriz 2:\n", matriz2)

# Sumar las matrices
suma_matriz = matriz1 + matriz2

print("La suma de las matrices es:\n", suma_matriz)

# Restar las matrices
resta_matriz = matriz1 - matriz2

print("La resta de las matrices es:\n", resta_matriz)

# Multiplicar las matrices
producto_hadamard = matriz1 * matriz2

print("El producto de Hadamard de las matrices es:\n", producto_hadamard)

# Dividir las matrices (elemento por elemento)
division_matriz = matriz1 / matriz2

print("La división elemento por elemento de las matrices es:\n", division_matriz)