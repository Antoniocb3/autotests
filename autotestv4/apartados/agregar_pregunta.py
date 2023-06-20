"""
Añadir pregunta al test.
Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.
Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.
Comprobamos que los datos son correctos,  para ello podríamos crear un objeto Question y si no lanza excepción es que
están bien.
Añadimos la pregunta al fichero en el formato que tenga (JSON o XML).
Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y escribimos de nuevo en el
fichero.


    Programa agregar_pregunta.py
    Autor: Antonio Carmona Bascón
    Fecha: 19/06/2023
"""

import json
import sys
import xml.etree.ElementTree as ET
from recuperar.autotests.autotestv1.v1.question import Question


def check_question_format(question_title, question_statement, options, base_score):
    try:
        Question(question_title, question_statement, options, base_score)
    except ValueError:
        print("El formato de la pregunta no es correcto.", file=sys.stderr)
        sys.exit(1)


def add_question(filename):
    NUMBER_OF_OPTIONS = 2
    if filename[-5:] == '.json':
        question_title = input("Introduce el titulo de la pregunta: ")
        base_score = int(input("Introduce la puntuación de la pregunta: "))
        question_statement = input("Introduce el enunciado de la pregunta: ")

        question_data = {  # crea un diccionario y le asigna los valores correspondientes
            'name': question_title,
            'base_score': base_score,
            'statement': question_statement,
            'options': []
        }
        for i in range(NUMBER_OF_OPTIONS):
            option = input(f"Escribe la opción {i + 1}: ")
            weight = input(f"Escribe el valor de la opción {i + 1}: ")
            option_data = {
                'option': option,
                'weight': weight
            }
            question_data['options'].append(option_data)  # agrega el dic 'option_data' a la lista de opciones
            # 'options' de 'question_data'

        with open(filename, 'r') as f:
            try:
                questions = json.load(f)
            except ValueError:
                questions = []

        questions.append(question_data)

        with open(filename, 'w') as f:
            json.dump(questions, f, indent=2)

    if filename[-4:] == ".xml":
        lista_opciones = []

        tree = ET.parse(filename)
        root = tree.getroot()
        question_title = input("Introduce el titulo de la pregunta: ")
        base_score = input("Introduce la puntuación de la pregunta: ")
        question_statement = input("Introduce el enunciado de la pregunta: ")

        name = ET.Element('Pregunta', {'name': question_title, 'base_score': str(base_score)})
        statement = ET.SubElement(name, 'statement')
        statement.text = question_statement
        options = ET.SubElement(statement, 'options')

        for i in range(NUMBER_OF_OPTIONS):
            option = input(f"Escribe la opción {i + 1}: ")
            weight = input(f"Escribe el valor de la opción {i + 1}: ")
            posible_option = ET.SubElement(options, 'option', {'weight': weight})
            posible_option.text = option
            lista_opciones.append((option, float(weight)))

        check_question_format(question_title, question_statement, lista_opciones, int(base_score))

        root.append(name)
        ET.indent(root, space='  ')
        tree.write(filename, encoding='utf-8', xml_declaration=True)
