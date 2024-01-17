def tem():
    print("Hola desde mi modulo.py")
def main():
    print("Doy una funcion y hago algo")
    #tem()
    #tem2()
def tem2():
    print("Adios desde mi modulo.py")

#No es necesario ejecutar las funciones fuera del main, solo dentro de esa funcion
if __name__=="__main__":
    main()

