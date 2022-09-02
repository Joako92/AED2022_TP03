"""De cada proyecto se conoce:
    • Número de proyecto
    • Título
    • Fecha de actualización con el formato dd-mm-yyyy validando que el año esté entre 2000 y 2022
    • Lenguaje(siendo 0:Python, 1:Java, 2:C++, 3:Javascript, 4:Shell, 5:HTML, 6:Ruby, 7:Swift, 8: C#, 9:VB, 10:Go)
    • Cantidad de líneas de código"""


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
