"""
--Archivo main.py--
Archivo principal el cual hereda las clases y funciones del archivo
operaciones.py, de igual manera este recive tres paremtros:

numero1   =   Valor introducido por teclado por el usuario
numero2   =   Valor introducido por teclado por el usuario
opcion    =   Es la eleccion de la operacion matematica a realizar

En esta seccion se encuentra la ejecucion de un menu de opciones
por medio de condicionales if, con sus respectivas validaciones
"""

from operaciones import Operaciones

try:
    contador = 0
    
    #Opcion matematica ha elegir
    while contador == 0:
        print("--------CALCULADORA--------")
        print("\nEliga una opcion : ")
        print("""
            1-Sumar
            2-Restar
            3-Multiplicar
            4-Dividir
            5-Potencia
            6-Porcentaje
            7-Raiz Cuadrada
            8-Factorial""")
        opcion=int(input("Opcion : "))

        if opcion <1 or opcion >8:
            print("\nDebes elegir una de las opciones anteriores!")            
        else:
            contador += 1

    #Datos ingresados por el usuario
    numero1 = int(input("\nIngrese un numero : "))
    numero2 = int(input("Ingrese el siguiente numero : "))
    Result = Operaciones(numero1, numero2)

    #Menu de opciones   
    if (opcion == 1):
        print(f"\nSuma : {Result.suma()}")
    elif (opcion == 2):
        print(f"\nResta : {Result.resta()}")
    elif (opcion == 3):
        print(f"\nMultiplicacion : {Result.multiplicacion()}")
    elif (opcion == 4):
        print(f"\nDivision : {Result.division()}")
    elif (opcion == 5):
        print(f"\nPotencia de {numero1}^{numero2} : {Result.potencia()}")
    elif (opcion == 6):
        print(f"\nPorcentaje : {Result.porcentaje()}")
    elif (opcion == 7):
        print(f"\nRaiz Cuadrada : {Result.raizCuadrada()}")
    elif (opcion == 8):
        print(f"\nFactorial : {Result.factorial()}")
    else:
        print("Debes elegir una de las opciones anteriores!\n")        
except ValueError:
    print("¡Exite un error! \n-->Debes ingresar un valor numerico")