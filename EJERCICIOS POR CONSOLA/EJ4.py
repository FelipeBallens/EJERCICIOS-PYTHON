print("EJERCICIO 4. ELECCION ROBOTS Y ARTICULACIONES: \n")
# MENU ELECCION ROBOTS
print("\t\t\t\t**************")
print("\t\t\t\t*** ROBOTS ***")
print("\t\t\t\t**************")
print("************************************************************************************")
print("\t1.ROBOT CILINDRICO")
print("\t2.ROBOT CARTESIANO")
print("\t3.ROBOT ESFERICO")
print("************************************************************************************\n")
Eleccion = int(input("Digite el numero del robot del que quiere saber sus articulaciones: "))
print("\n************************************************************************************\n")

if Eleccion == 1 :
        print("EL ROBOT CILINDRICO TIENE 1 ARTICULACION ROTACIONAL Y 2 ARTICULACIONES PRISMATICAS")
        print("\n************************************************************************************")
elif Eleccion == 2:
        print("EL ROBOT CARTESIANO TIENE 3 ARTICULACIONES PRISMATICAS")
        print("\n************************************************************************************")
elif Eleccion == 3:
        print("EL ROBOT ESFERICO TIENE 2 ARTICULACIONES ROTACIONALES Y 1 ARTICULACION PRISMATICA")
        print("\n************************************************************************************")


