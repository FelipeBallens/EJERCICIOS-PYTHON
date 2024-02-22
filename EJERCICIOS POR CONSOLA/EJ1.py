print("EJERCICIO 1. CALCULAR LA POTENCIA DE UN CIRCUITO: \n") ## descripcion
# SOLICITAR AL USUARIO VALORES DE VOLTAJE Y CORRIENTE
Voltaje = input("Digite el valor de Voltaje en voltios: \t")
Corriente = input("Digite el valor de la Corriente en Amperios: \t")
# CONVERTIR VALORES A FLOTANTES Y REALIZAR OPERACION
Potencia = float(Voltaje) * float(Corriente)
# IMPRIMIR POTENCIA RESULTANTE
print("La potencia del circuito es: ", Potencia)

