"""
En esta segunda versión el fichero de preguntas va a ser json, se adjunta un ejemplo. Adecuar la ejecución del test a
este fichero en vez de al que se había propuesto inicialmente.

    Programa autotestv2.py
    Autor: Antonio Carmona Bascón
    Fecha: 19/06/2023
"""

from recuperar.autotests.autotestv1.v1.question import Question, QuestionError
import json
import time

TOTAL_SCORE = 0
with open('test.json', 'r') as file:
    # Carga el contenido del fichero como una lista de diccionarios
    json_file = json.load(file)

for q in json_file:
    options = q['options']
    q['options'] = [(str(option), float(score)) for option, score in options]

    name = q['name']
    statement = q['statement']
    options = q['options']
    points = q['points']

    question = Question(name, statement, options, points)

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

print(f'La puntuación total es de {TOTAL_SCORE / len(json_file) * 10} / 10')
