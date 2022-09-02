def validar_vacio(num):
    if num.strip() == "":
        return False
    return True


def validar_numero(num):
    if num.isdigit():
        return True
    return False


def validar_positivo(num):
    if int(num) < 1:
        return False
    return True


def validar_conjunto(inf, sup, num):
    if inf > int(num) or int(num) > sup:
        return False
    return True


def validar():
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
