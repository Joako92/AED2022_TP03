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


def validar():
    num = int(input("Ingrese un numero mayor a 0: "))
    while num < 1:
        print("Error...")
        num = int(input("Ingrese un numero mayor a 0: "))
    return num


def validar_entre(inf, sup):
    num = int(input(f"Ingrese un numero entre {inf} y {sup}: "))
    while inf > num or num > sup:
        print("Error...")
        num = int(input(f"Ingrese un numero entre {inf} y {sup}: "))
    return num


def cargar_fecha():
    dia = 0
    while dia <= 0 or dia >= 31: 
        dia = int(input("Ingrese dia (DD): "))
    mes = 0
    while mes <= 0 or mes >= 13:
        mes = int(input("Ingrese mes (MM): "))
    anio = 0
    while anio <= 1999 or anio >= 2023:
        anio = int(input("Ingrese año (AAAA): "))

    return f"{dia:<2}/{mes:<2}/{anio:<4}"


def generar_titulo():
    letras = ("A", "B", "C", "D", "E")
    return f"{random.choice(letras)}{random.choice(letras)}{random.choice(letras)}{random.randint(100, 999)}"


def carga_manual(v_proy, cant):
    for i in range(cant):
        numero = int(input("Ingrese numero para el proyecto: "))
        titulo = input("Ingrese titulo del proyecto: ")
        fecha = cargar_fecha()
        leng = input("Ingrese codigo del lenguaje (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go): ")
        cant_lineas = int(input("Ingrese cantidad de lineas del codigo: "))
        v_proy.append(Modulo.Proyecto(numero, titulo, fecha, leng, cant_lineas))


def carga_auto(v_proy, cant):
    for i in range(cant):
        numero = random.randint(1000, 9999)
        titulo = generar_titulo()
        fecha = f"{random.randint(10, 30)}/{random.randint(1, 12)}/{random.randint(2000, 2022)}"
        leng = random.randint(0, 10)
        cant_lineas = random.randint(100, 999)
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


def opcion3():
    pass


def opcion4():
    pass


def opcion5():
    pass


def opcion6():
    pass


def opcion7():
    pass


def menu():
    # Iniciar el vector que contiene los proyectos
    v_proyectos = []
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
                    opcion3()
                    input("Pulse enter para continuar...")

                elif op == 4:
                    opcion4()
                    input("Pulse enter para continuar...")

                elif op == 5:
                    opcion5()
                    input("Pulse enter para continuar...")

                elif op == 6:
                    opcion6()
                    input("Pulse enter para continuar...")

                elif op == 7:
                    opcion7()
                    input("Pulse enter para continuar...")

        if op == 8:
            print("--- Programa finalizado ---")


if __name__ == '__main__':
    menu()
