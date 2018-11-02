
def Menu():
    """Funcion que Muestra el Menu"""
    print("""************
Calculadora

Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")
def Calculadora():

    Menu()
    Opcion = int(input("Selecione Opcion"))
    while (Opcion >0 and Opcion <5):
        x = int(input("Ingrese Numero"))
        y = int(input("Ingrese Otro Numero"))
        if (Opcion==1):
            print ("La Suma es:", x+y)
            Opcion = int(input("Selecione Opcion"))
        elif(Opcion==2):
            print ("La Resta es:",x-y)
            Opcion = int(input("Selecione Opcion"))
        elif(Opcion==3):
            print ("La Multiplicacion es:",x*y)
            Opcion = int(input("Selecione Opcion"))
        elif(Opcion==4):
            try:
              print("La Division es:", x/y)
              Opcion = int(input("Selecione Opcion"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              Opcion = int(input("Selecione Opcion"))
Calculadora()