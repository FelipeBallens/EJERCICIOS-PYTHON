import numpy as np
import matplotlib.pyplot as plt

# Crear un rango de temperaturas desde -200°C a 200°C con 1000 valores dentro del arreglo
temperaturas = np.linspace(-200, 200, 1000)

# Ecuación de Callendar-Van Dusen
A = 3.9083e-3
B = -5.775e-7
R0 = 100  # Resistencia a 0 grados Celsius
resistencias = R0 * (1 + A*temperaturas + B*temperaturas**2) # calcular las resistencias para cada temperatura del arreglo temperaturas

plt.plot(temperaturas, resistencias) # graficar en funcion de temperaturas y resistencias
plt.xlabel('Temperatura (°C)') # Nombrar los ejes
plt.ylabel('Resistencia (Ω)')  # Nombrar los ejes
plt.title('Comportamiento de una PT100') #titulo grafico
plt.grid(True) # mostrar cuadricula
plt.show() #mostrar grafico