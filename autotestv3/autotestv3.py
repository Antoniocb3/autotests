"""
Esta versión hará lo mismo que la versión 2, pero con ficheros XML.

Se adjunta un fichero XML de muestra.

Tened en cuenta que el atributo name correspondiente a la pregunta podría no estar y en este caso el nombre de la
pregunta es la cadena vacía.

    Programa autotest3.py
    Autor: Antonio Carmona Bascón
    Fecha: 19/06/2023
"""

import xml.etree.ElementTree as ET
from recuperar.autotests.autotestv1.v1.question import Question, QuestionError
import time

TOTAL_SCORE = 0
file_name = 'test.xml'
file = ET.parse(file_name)
root = file.getroot()
for i in range(len(root)):
    name = root[i].get('name')
    base_score = root[i].get('base_score')
    statement = root[i][0].text.strip()
    options = root[i][1]
    options_list = []
    for j in range(len(options)):
        option = root[i][1][j].text.strip()
        weight = root[i][1][j].get('weight')
        options_list.append((option, float(weight)))

    question = Question(name, statement, options_list, int(base_score))

    print()
    print("--------------------------------------------")
    print(question.question_name)
    print("--------------------------------------------")
    print(question.statement)
    for option in question.posible_answer:
        print(f' - {option[0]}')
    try:
        answer = int(input('¿Cuál es la respuesta correcta?: '))
        time.sleep(0.5)
        question_score = question.get_score(answer)
        print(f'Puntuación obtenida: {question_score}')
        TOTAL_SCORE += question_score
    except ValueError:
        print("La respuesta introducida no es válida")
    except QuestionError as e:
        print(f'ERROR: {e}')

print(f'La puntuación total es de {TOTAL_SCORE / len(root) * 10} / 10')
