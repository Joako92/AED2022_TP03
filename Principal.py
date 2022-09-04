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
    fin_mes = obtener_dias_por_mes_y_anio(mes, anio)
    mes = dos_digitos(mes)
    dia = validar_entre(1, fin_mes)
    dia = dos_digitos(dia)

    return f"{dia:<2}/{mes:<2}/{anio:<4}"


def generar_titulo():
    letras = ("A", "B", "C", "D", "E")
    return f"{random.choice(letras)}{random.choice(letras)}{random.choice(letras)}{random.randint(100, 999)}"


def numero_unico(v_proy, num):
    # Validar qe el numero no este repetido en el arreglo
    n = len(v_proy)
    for i in range(n):
        if v_proy[i].numero == num:
            return False
    return True


def carga_manual(v_proy, cant):
    for i in range(cant):
        print(f"\nIngrese numero para el proyecto {i+1}...")
        numero = validar()
        while not numero_unico(v_proy, numero):
            print("Numero de proyecto repetido...")
            numero = validar()

        titulo = input(f"Ingrese titulo del proyecto {numero}: ")
        fecha = cargar_fecha()
        leng = seleccionar_lenguaje()
        print("Ingrese cantidad de lineas del codigo...")
        cant_lineas = validar()
        v_proy.append(Modulo.Proyecto(numero, titulo, fecha, leng, cant_lineas))


def carga_auto(v_proy, cant):
    for i in range(cant):
        numero = random.randint(1000, 9999)
        while not numero_unico(v_proy, numero):
            numero = random.randint(1000, 9999)
        titulo = generar_titulo()
        fecha = f"{dos_digitos(random.randint(1, 30))}/{dos_digitos(random.randint(1, 12))}/{random.randint(2000, 2022)}"
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


def seleccionar_lenguaje():
    print("Ingrese numero del lenguaje que desea listar siendo:")
    
    lenguajes = Modulo.obtener_lenguajes()
    for i in range(len(lenguajes)):
        print(f"\t - {i}: {lenguajes[i]}")

    return validar_entre(0, len(lenguajes)-1)


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
    v_leng = [0] * (len(Modulo.obtener_lenguajes()))  # Crear vector de ceros
    n = len(v_proy)
    for i in range(n):
        v_leng[v_proy[i].lenguaje] += v_proy[i].cant_lineas

    print("{:<20}N° DE LINEAS".format("LENGUAJE"))
    for i in range(len(v_leng)):
        print(f"-{Modulo.lenguaje(i):<20} -{v_leng[i]}")


def contar_por_anio(v_proy):
    anios = [0] * 23
    for i in range(len(v_proy)):
        fecha = v_proy[i].fecha
        if fecha[-2] == 0:
            ids = int(fecha[-1])
        else:
            ids = int(fecha[-2] + fecha[-1])
        anios[ids] += 1
    
    return anios


def resumen_anio(v_proyectos):
    anios = contar_por_anio(v_proyectos)

    print("{:<8}{:<5}".format("AÑO", "CANT PROYECTOS"))
    for i in range(len(anios)):
        if anios[i] > 0:
            anio = 2000 + i
            print(f"-{anio:<8}{anios[i]}")
            # print('En el año', anio, 'se generaron', anios[i], 'proyectos')


def listar_leng(v_proy):
    ln = seleccionar_lenguaje()
    n = len(v_proy)
    for i in range(n-1):
        for j in range(i+1, n):
            if v_proy[j].numero < v_proy[i].numero:
                v_proy[i], v_proy[j] = v_proy[j], v_proy[i]

    print(Modulo.encabezado())
    for i in range(n):
        if v_proy[i].lenguaje == ln:
            print(Modulo.to_string(v_proy[i]))


def opcion7(v_proy):
    anios = contar_por_anio(v_proy)

    may = None
    for i in range(len(anios)):
        if may is None or anios[i] > may:
            may = anios[i]
    
    print('\nAños con mayor cantidad de proyectos actualizados: ')
    for i in range(len(anios)):
        if anios[i] == may:
            anio = 2000 + i
            print('\t- Año', anio, 'con', may, 'proyectos')


# Mostrar menu y solicitar opcion
def mostrar_menu():
    menu = f"""\nMenu de opciones
        {"-" * 50}
        1. Cargar proyectos
        2. Listar proyectos
        3. Actualizar proyecto
        4. Resumen por lenguaje
        5. Resumen por año
        6. Filtrar lenguaje
        7. Productividad
        8. Salir
        {"-" * 50}
        Ingrese opcion...
        """
    print(menu)
    op = validar_entre(1, 8)

    return op


def principal():
    # Iniciar el vector que contiene los proyectos
    v_proyectos = []
    op = 0
    while op != 8:
        op = mostrar_menu()

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

        if op == 8:
            print("--- Programa finalizado ---")

        else:
            if len(v_proyectos) == 0:
                print("Aun no se han cargado proyectos...")

            else:
                if op == 2:
                    listar(v_proyectos)
                elif op == 3:
                    buscar_numero(v_proyectos)
                elif op == 4:
                    resumen(v_proyectos)
                elif op == 5:
                    resumen_anio(v_proyectos)
                elif op == 6:
                    listar_leng(v_proyectos)
                elif op == 7:
                    opcion7(v_proyectos)
            
        input("\n>>Pulse enter para continuar...")


if __name__ == '__main__':
    principal()
