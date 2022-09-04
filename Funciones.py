def validar_vacio(num):
    if num.strip() == "":
        return False
    return True


def validar_numero(num):
    if num.isdigit():
        return True
    return False


def validar_positivo(num):
    return int(num) > 0


def validar_conjunto(inf, sup, num):
    return inf <= int(num) <= sup


def validar(): # Validar que sea un numero entero positivo
    num = input("Ingrese un numero mayor a 0: ")
    while not validar_vacio(num) or not validar_numero(num) or not validar_positivo(num):
        print("Error...")
        num = input("Ingrese un numero mayor a 0: ")

    return int(num)


def validar_entre(inf, sup):
    num = input(f"Ingrese un numero entre {inf} y {sup}: ")
    while not validar_vacio(num) or not validar_numero(num) or not validar_conjunto(inf, sup, num):
        print("Error...")
        num = input(f"Ingrese un numero entre {inf} y {sup}: ")

    return int(num)


def es_anio_bisiesto(anio):
    return anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0


def obtener_dias_por_mes_y_anio(mes, anio):
    if mes in (1, 3, 5, 7, 8, 10, 12):  # meses con 31 dias
        return 31
    elif mes in (4, 6, 9, 11):  # meses con 30 dias
        return 30
    elif es_anio_bisiesto(anio):
        return 29
    else:
        return 28


def dos_digitos(d):
    if d < 10:
        d = "0" + str(d)
    return d
