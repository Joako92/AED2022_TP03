"""1)Cargar proyectos:La generación de n proyectos de software cargados en un arreglo de registros.
Para ello se pueden generar los datos totalmente aleatorios
o bien contar con proyectos completos precargados e ir seleccionando aleatoriamente entre los mismos.
Cada vez que selecciona esta opción durante la ejecución se agregarán datos al arreglo,
sin eliminar los que ya estaban cargados. El número del proyecto no debe repetirse dentro del arreglo.

2)Listar proyectos:Mostrar todos los proyectos contenidos en el arreglo,
pero ordenados alfabéticamente por título.
Cada proyecto debe ocupar un máximo de dos líneas en pantalla
y en lugar de mostrarse el identificador del lenguaje se debe mostrar su nombre.

3)Actualizar proyecto: Buscar si existe un proyecto con número x,
siendo x un valor que se ingrese por teclado.
Si existe, se debe permitir modificar su cantidad de líneas de código
y la fecha de actualización (recuerde que debe cumplir con el formato dd-mm-yyyy).
Si no existe, debe indicar con un mensaje.

4)Resumen por lenguaje: Calcular la cantidad de líneas de código acumuladas por lenguaje.
Mostrar los resultados teniendo en cuenta que se debe visualizar el nombre del lenguaje en lugar del código.

5)Resumen por año: Calcular la cantidad de proyectos por año de actualización,
considerando los años entre 2000 y 2022 inlcuidos ambos.
Mostrar los resultados sólo de los años que tengan algún proyecto de software.

6)Filtrar lenguaje: Mostrar los proyectos de software ordenados por número de proyecto de manera ascendente,
del lenguaje ln, siendo ln un valor ingresado por teclado.

7)Productividad: A partir del resultado obtenido en el punto 5,
determinar el año con mayor cantidad de proyectos actualizados,
considerando mostrar todos los años si fuera más de uno con dicha cantidad."""
import random
import Modulo
from Funciones import *


def cargar_fecha():
    print("Ingrese año (AAAA)...")
    anio = validar_entre(2000, 2022)
    print("Ingrese mes (MM)...")
    mes = validar_entre(1, 12)
    print("Ingrese dia (DD)...")
    dia = validar_entre(1, 31)

    return f"{dia:<2}/{mes:<2}/{anio:<4}"


def generar_titulo():
    letras = ("A", "B", "C", "D", "E")
    return f"{random.choice(letras)}{random.choice(letras)}{random.choice(letras)}{random.randint(100, 999)}"


def carga_manual(v_proy, cant):
    for i in range(cant):
        numero = int(input("Ingrese numero para el proyecto: "))
        titulo = input("Ingrese titulo del proyecto: ")
        fecha = cargar_fecha()
        leng = int(input("Ingrese codigo del lenguaje (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go): "))
        cant_lineas = int(input("Ingrese cantidad de lineas del codigo: "))
        if v_proy[0] is None:
            v_proy[0] = Modulo.Proyecto(numero, titulo, fecha, leng, cant_lineas)
        else:
            v_proy.append(Modulo.Proyecto(numero, titulo, fecha, leng, cant_lineas))


def carga_auto(v_proy, cant):
    for i in range(cant):
        numero = random.randint(1000, 9999)
        titulo = generar_titulo()
        fecha = f"{random.randint(10, 30)}/{random.randint(1, 12)}/{random.randint(2000, 2022)}"
        leng = random.randint(0, 10)
        cant_lineas = random.randint(100, 999)
        if v_proy[0] is None:
            v_proy[0] = Modulo.Proyecto(numero, titulo, fecha, leng, cant_lineas)
        else:
            v_proy.append(Modulo.Proyecto(numero, titulo, fecha, leng, cant_lineas))


def listar(v_proy):
    n = len(v_proy)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_proy[i].titulo > v_proy[j].titulo:
                v_proy[i], v_proy[j] = v_proy[j], v_proy[i]

    print(Modulo.encabezado())
    for i in range(n):
        print(Modulo.to_string(v_proy[i]))


def buscar_numero(v_proy):
    print("Ingrese numero de proyecto buscado...")
    num = validar()
    n = len(v_proy)
    encontro = False
    for i in range(n):
        if v_proy[i].numero == num:
            encontro = True
            print("Proyecto encontrado...")
            print("Ingrese nueva cantidad de lineas de codigo...")
            cant_n = validar()
            print("Cantidad anterior: ", v_proy[i].cant_lineas)
            print("Cantidad nueva: ", cant_n)
            v_proy[i].cant_lineas = cant_n
            print()
            print("Ingrese nueva fecha: ")
            fecha_n = cargar_fecha()
            print("Fecha anterior: ", v_proy[i].fecha)
            print("Fecha nueva: ", fecha_n)
            v_proy[i].fecha = fecha_n

    if not encontro:
        print("No hubo coincidencias...")


def resumen(v_proy):
    v_leng = [0] * 11
    n = len(v_proy)
    for i in range(n):
        v_leng[v_proy[i].lenguaje] += v_proy[i].cant_lineas

    for i in range(len(v_leng)):
        print(f"Lenguaje: {Modulo.lenguaje(i):<20}-Cantidad de lineas: {v_leng[i]}")


def opcion5():
    pass


def listar_leng(v_proy):
    print("Ingrese numero del lenguaje que desea listar (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)...")
    ln = validar_entre(0, 10)
    n = len(v_proy)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_proy[j].numero < v_proy[i].numero:
                v_proy[i], v_proy[j] = v_proy[j], v_proy[i]

    print(Modulo.encabezado())
    for i in range(n):
        if v_proy[i].lenguaje == ln:
            print(Modulo.to_string(v_proy[i]))


def opcion7():
    pass


def menu():
    # Iniciar el vector que contiene los proyectos
    v_proyectos = [None]
    op = 0
    while op != 8:
        print("\nMENU DE OPCIONES")
        print("-" * 50)
        print('1. Cargar proyectos')  # Debe permitir la carga manual o automatica
        print('2. Listar proyectos')
        print('3. Actualizar proyecto')
        print('4. Resumen por lenguaje')
        print('5. Resumen por año')
        print('6. Filtrar lenguaje')
        print('7. Productividad')
        print('8. Salir')
        print("-" * 50)
        print('Ingrese opcion...')
        op = validar_entre(1, 8)

        if op == 1:
            print("Ingrese la cantidad de proyectos que desea controlar...")
            cant = validar()
            print("Ingrese 1 para carga manual - 2 para carga automatica...")
            elec = validar_entre(1, 2)
            if elec == 1:
                carga_manual(v_proyectos, cant)
            if elec == 2:
                carga_auto(v_proyectos, cant)
            print("---Carga completa---")
            input("Pulse enter para continuar...")

        else:
            if v_proyectos[0] is None:
                print("Aun no se han cargado proyectos...")

            else:
                if op == 2:
                    listar(v_proyectos)
                    input("Pulse enter para continuar...")

                elif op == 3:
                    buscar_numero(v_proyectos)
                    input("Pulse enter para continuar...")

                elif op == 4:
                    resumen(v_proyectos)
                    input("Pulse enter para continuar...")

                elif op == 5:
                    opcion5()
                    input("Pulse enter para continuar...")

                elif op == 6:
                    listar_leng(v_proyectos)
                    input("Pulse enter para continuar...")

                elif op == 7:
                    opcion7()
                    input("Pulse enter para continuar...")

        if op == 8:
            print("--- Programa finalizado ---")


if __name__ == '__main__':
    menu()
