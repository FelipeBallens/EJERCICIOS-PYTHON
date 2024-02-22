import math

pi = math.pi
print("EJERCICIO 3. CALCULO DE VOLUMENES: \n")
# MENU ELECCION DE SOLIDOS
print("Solidos: \n")
print("1. Prisma\n")
print("2. Piramide\n")
print("3. Cono truncado\n")
print("4. Cilindro\n")
# ELECCION SOLIDOS
Eleccion = int(input("Ingrese el numero del solido: "))
# CONDICIONALES PARA CARACTERISTICAS SOLIDO
if Eleccion==1:
    print("\n****************************************************************")
    print("PRISMA\n")
    Base = float(input("Digite el valor del area de la base del prisma: "))
    Altura = float(input("\nDigite el valor de la altura del prisma: "))
    Vprisma = Base * Altura 
    print("\nEl volumen del prisma es: ", Vprisma)
    print("\n****************************************************************\n") ## descripcion

elif Eleccion==2:
    print("\n****************************************************************")
    print("PIRAMIDE\n")
    Base = float(input("Digite el valor del area de la base de la piramide: "))
    Altura = float(input("\nDigite la altura de la piramide: "))
    VPiramide = (Base * Altura)/3
    print("\nEl volumen de la piramide es: ", VPiramide) 
    print("\n****************************************************************\n")

elif Eleccion==3:
    print("\n****************************************************************")
    print("\nCONO TRUNCADO\n")
    Altura = float(input("\nDigite la altura del cono truncado: "))
    Radio1 = float(input("\nDigite el radio de la base del cono: "))
    Radio2 = float(input("\nDigite el radio de la punta del cono: "))
    Vcono = ((Altura*pi)/3)*((math.pow(Radio1,2))+(math.pow(Radio2,2))+(Radio1*Radio2))
    print("\nEl volumen del cono es: ", Vcono) 
    print("\n****************************************************************\n")

elif Eleccion==4:
     print("\n****************************************************************")
     print("\nCILINDRO\n")
     Altura = float(input("\nDigite la altura del cilindro: "))
     Radio1 = float(input("\nDigite el radio del cilindro: "))
     Vcilindro = (pi)*(math.pow(Radio1,2))*(Altura)
     print("\nEl volumen del cilindro es: ", Vcilindro) 
     print("\n****************************************************************\n")