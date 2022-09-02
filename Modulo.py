"""De cada proyecto se conoce:
    • Número de proyecto
    • Título
    • Fecha de actualización con el formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
    • Lenguaje(siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
    • Cantidad de líneas de código"""
import random


class Proyecto:
    def __init__(self, num, tit, fech, leng, cant):  # Setter
        self.numero = num
        self.titulo = tit
        self.fecha = fech  # formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
        self.lenguaje = leng  # (siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
        self.cant_lineas = cant


def to_string(proyecto):  # Esto tendria que ser un getter
    # en lugar de mostrarse el identificador del lenguaje se debe mostrar su nombre
    return f"{proyecto.numero:<10}{proyecto.titulo:<20}{proyecto.fecha:<15}{lenguaje(proyecto.lenguaje):<15}{proyecto.cant_lineas:<8}"


def encabezado():
    # Devuelve los titulos para poner sobre la funcion to_string()
    return "{:<10}{:<20}{:<15}{:<15}{:<8}".format("N°", "Titulo", "Fecha", "Lenguaje", "Lineas")


def lenguaje(leng):
    lenguajes = ("Python", "Java", "C++", "Javascript", "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go")
    return lenguajes[int(leng)]


def generar_proyectos(cantidad, array):  # Esto genera los 'n' proyectos de forma aleatoria
    for i in range(cantidad):
        # Numero
        flag = True
        while flag:
            num= random.randint(1, 1000000)

            # si existe registro en el array, se comprueba que el numero no se repita
            if len(array) > 0:
                flag = False
                for j in range(len(array)):
                    if array[j].numero == num:
                        flag = True

                    else:
                        pass

                if flag:
                    pass

                else:
                    # si existe registro, pero el numero no se repite, sale
                    break

            else:
                # si no existe registro no comprueba nada
                break

        # Titulo
        tit = 'Proyecto ' + str(num)

        # Fecha
        mes= random.randint(1, 12)

        if mes in (1, 3, 5, 7, 8, 10, 12):
            dia= random.randint(1, 31)

        elif mes == 2:
            dia= random.randint(1, 28)

        else:
            dia= random.randint(1, 30)

        agno= random.randint(2000, 2022)

        fech= str(dia) + '-' + str(mes) + '-' + str(agno)

        # Lenguaje
        leng= random.randint(0, 10)

        # Cantidad Lineas
        cant= random.randint(1, 1000000)

        obj= Proyecto(num, tit, fech, leng, cant) # Crea el objeto

        array.append(obj)   # Añade a la lista

    return
