"""
Necesitamos crear los ficheros (JSON o XML) donde guardar las preguntas del test. Editarlos directamente puede ser una
labor un poco engorrosa, así que vamos a hacer un programa que nos facilite la tarea.

Nuestro programa mostrará un menú con las siguientes opciones:

1. Crear fichero de test.
Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos.
Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
Finalmente se creará el fichero correspondiente.

2. Seleccionar fichero de test.
Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos.
Pensad que estos dos apartados son iguales que la opción anterior, igual podemos modularizar para ahorrar código.
Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error.

3. Añadir pregunta al test.
Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.
Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.
Comprobamos que los datos son correctos,  para ello podríamos crear un objeto Question y si no lanza excepción es que
están bien.
Añadimos la pregunta al fichero en el formato que tenga (JSON o XML).
Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en el
fichero.


    Programa autotestv4.py
    Autor: Antonio Carmona Bascón
    Fecha: 19/06/2023
"""

from recuperar.autotests.autotestv4.menu import Menu
from recuperar.autotests.autotestv4.apartados.crear_fichero import create_file
from recuperar.autotests.autotestv4.apartados.seleccionar_fichero import choose_filename
from recuperar.autotests.autotestv4.apartados.agregar_pregunta import add_question


def main():
    filename = ''
    menu = Menu("Crear fichero de test", "Seleccionar fichero de test", "Añadir pregunta al test", "Terminar",
                title="Menú autotest")
    while True:
        opc = menu.choose()
        match opc:
            case 1:
                filename = create_file()
            case 2:
                try:
                    filename = choose_filename()
                except FileNotFoundError:
                    print(f'El fichero no existe \n')
            case 3:
                if filename == '':
                    print('Debes seleccionar o crear un fichero antes \n')
                add_question(filename)
            case _:
                break
    print("Hasta la próxima :-)")


if __name__ == '__main__':
    main()
