"""
Seleccionar fichero de test.
Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos.
Pensad que estos dos apartados son iguales que la opción anterior, igual podemos modularizar para ahorrar código.
Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error.

    Programa seleccionar_fichero.py
    Autor: Antonio Carmona Bascón
    Fecha: 19/06/2023
"""

from recuperar.autotests.autotestv4.apartados.crear_fichero import check_if_file_exist


def choose_filename():
    while True:
        file = input('Escribe el archivo que quieras seleccionar: ')
        if file[-5:] == ".json" or file[-4:] == ".xml":
            if not check_if_file_exist(file):
                raise FileNotFoundError('El fichero no existe')
            break
        else:
            print("ERROR. La extensión debe ser '.json' o '.xml'")
    return file


if __name__ == '__main__':
    choose_filename()
