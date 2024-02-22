#Cálculo de resistencia de una RTD PT100 en función de la temperatura
## descripcion
def resistencia_PT100(temperatura):
    # Coeficientes de la ecuación de Callendar-Van Dusen
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12

    # Resistencia a 0°C
    R0 = 100.0  # en ohmios

    # Calcula la resistencia en función de la temperatura utilizando la ecuación de Callendar-Van Dusen
    resistencia = R0 * (1 + A * temperatura + B * temperatura ** 2 + C * (temperatura - 100) * temperatura ** 3)
    return resistencia

temp = float(200) #Temperatura en grados celsius

# Calcular la resistencia para la temperatura dada
resistencia = resistencia_PT100(temp)

# Mostrar el resultado
print("La resistencia de la RTD a {:.2f}".format(temp), "°C es de: {:.2f}".format(resistencia), "ohmios")
