"""
Test para probar la clase Question

    Programa autotestv1.py
    Autor: Antonio Carmona Bascón
    Fecha: 17/05/2023
"""

import time
from recuperar.autotests.autotestv1.v1.question import Question, QuestionError

TOTAL_SCORE = 0

questions = [
    Question('Pais no EU', '¿Cuál de estos países no está en Europa?', [('Francia', -0.25), ('Australia', 1.0),
                                                                        ('Alemania', -0.25), ('Italia', -0.25)]),

    Question('Rey de los instrumentos', '¿Qué instrumento musical es conocido como el "rey de los '
                                        'instrumentos"?',
             [('Piano', 1.0), ('Guitarra', -0.25), ('Batería', -0.25), ('Violín', -0.25)]),

    Question('Raíz cuadrada', '¿Cuánto es la raíz cuadrada de 100?', [('5', -0.25), ('10', 1.0), ('7', -0.25)]),

    Question('Revolución Francesa', '¿En qué año se llevó a cabo la Revolución Francesa?', [('1789', 1.0),
                                                                                            ('1812', -0.25),
                                                                                            ('1848', -0.25),
                                                                                            ('1901', -0.25)]),

    Question('Pais no UE', '¿Cuál de estos países no es parte de la Unión Europea?', [('Polonia', -0.25),
                                                                                      ('Finlandia', -0.25),
                                                                                      ('Portugal', -0.25),
                                                                                      ('Noruega', 1.0)])
        ]
for question in questions:
    print()
    print("--------------------------------------------")
    print(question.question_name)
    print("--------------------------------------------")
    print(question.statement)
    for option in question.posible_answer:
        print(f' - {option[0]}')
    try:
        answer = int(input('¿Cuál es la respuesta correcta? (0 si no quieres responder): '))
        if answer == 0:
            question_score = 0
            time.sleep(0.5)
            print(f'Puntuación obtenida: {question_score}')
        else:
            time.sleep(0.5)
            question_score = question.get_score(answer)
            print(f'Puntuación obtenida: {question_score}')
            TOTAL_SCORE += question_score
    except ValueError:
        print('La respuesta introducida no es válida')
    except QuestionError as option:
        print(option)

print(f'La puntuación total es de {TOTAL_SCORE / len(questions) * 10} / 10')