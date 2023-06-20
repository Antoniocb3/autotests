"""
Crear fichero de test.
Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.
La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque este
programa únicamente maneja estos dos formatos.
Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.
Finalmente se creará el fichero correspondiente.

    Programa crear_fichero.py
    Autor: Antonio Carmona Bascón
    Fecha: 19/06/2023
"""
import os.path
import xml.etree.ElementTree as ET


def create_file():
    while True:
        filename = input("Dime el nombre del fichero?: ")
        if filename[-5:] == '.json':
            if not check_if_file_exist(filename):
                f = open(filename, 'w')
                f.close()
                print(f"Archivo '{filename}' creado con éxito")
                break
            else:
                overwrite = input(f"El archivo {filename} ya existe, si desea sobreescribirlo pulse 'S': ")
                if overwrite.upper() == "S":
                    f = open(filename, 'w')
                    f.close()
                    print(f"Fichero {filename} sobreescrito correctamente")
                    break
        elif filename[-4:] == '.xml':
            if not check_if_file_exist(filename):
                root = ET.Element('test')
                tree = ET.ElementTree(root)
                with open(filename, 'wb') as f:
                    tree.write(f, encoding='utf-8', xml_declaration=True)
                print(f"Archivo '{filename}' creado con éxito")
                break
            else:
                overwrite = input(f"El archivo {filename} ya existe, si desea sobreescribirlo pulse 'S': ")
                if overwrite.upper() == "S":
                    root = ET.Element('test')
                    tree = ET.ElementTree(root)
                    with open(filename, 'wb') as f:
                        tree.write(f, encoding='utf-8', xml_declaration=True)
                    print(f"Fichero {filename} sobreescrito correctamente")
                    break
        else:
            print("Tiene que tener extension .json o .xml")
    return filename


def check_if_file_exist(fichero):
    if os.path.exists(fichero):
        return True
    return False


if __name__ == '__main__':
    create_file()
