import numpy as np
import matplotlib.pyplot as plt
## descripcion
#Determina el tipo de sistema según el valor de zita
def tipo_sistema(zeta):
    if zeta < 1:
        return 'Subamortiguado'
    elif zeta == 1:
        return 'Críticamente amortiguado'
    else:
        return 'Sobreamortiguado'

#Calcula la respuesta de una función de transferencia de segundo orden.
def funcion_transferencia_segundo_orden(coeficientes, tiempo):
    K, wn, zeta = coeficientes
    if zeta < 1:
        wd = wn * np.sqrt(1 - zeta**2)
        salida = K * (1 - np.exp(-zeta * wn * tiempo) * (np.cos(wd * tiempo) + (zeta / np.sqrt(1 - zeta**2)) * np.sin(wd * tiempo)))
    elif zeta == 1:
        salida = K * (1 - np.exp(-wn * tiempo) * (1 + wn * tiempo))
    else:
        wd = wn * np.sqrt(zeta**2 - 1)
        salida = K * (1 - (1 / (2 * zeta * np.sqrt(zeta**2 - 1))) * np.exp(-zeta * wn * tiempo) * (np.exp(wd * tiempo) - np.exp(-wd * tiempo)))
    return salida

# Coeficientes de la función de transferencia (K, wn, zeta)
K = float(input("Ingrese el coeficiente K: "))
wn = float(input("Ingrese la frecuencia natural wn: "))
zeta = float(input("Ingrese la razón de amortiguamiento zeta: "))

# Tipo de sistema
tipo = tipo_sistema(zeta)
print("\nTipo de sistema:", tipo)

# Tiempo de respuesta
tiempo = np.linspace(0, 10, 1000)

# Respuesta de la función de transferencia
respuesta = funcion_transferencia_segundo_orden([K, wn, zeta], tiempo)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(tiempo, respuesta, label='Respuesta')
plt.title('Respuesta de la función de transferencia de segundo orden')
plt.xlabel('Tiempo')
plt.ylabel('Respuesta')
plt.grid(True)
plt.legend()
plt.show()
