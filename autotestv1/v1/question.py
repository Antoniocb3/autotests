"""
Se pretende crear una aplicación que haga exámenes tipo test similares a como los realiza la
plataforma Moodle con una sola respuesta. Esta plataforma permite crear un cuestionario, añadirle
preguntas, ejecutarlo y dar una calificación.

Empezaremos creando una clase para modelar las preguntas, los objetos de esta clase (Question)
tendrán los siguientes atributos:
• Nombre de la pregunta.
• Enunciado.
• Elecciones (posibles respuestas): lista de tuplas (texto respuesta, calificación en % [0,1]).
• Puntuación base de la pregunta (por defecto 1).
El comportamiento de esta clase permite:
• Obtener la puntuación de la pregunta enviándole la opción escogida y, en caso de tener otra
puntuación base, la puntuación correspondiente.
• Esta clase es inmutable.
• Podrá tener las propiedades necesarias para conocer el valor de los atributos que hagan falta.

    Programa question.py
    Autor: Antonio Carmona Bascón
    Fecha: 19/06/2023
"""

from typeguard import typechecked


class QuestionError(Exception):
    def __init__(self):
        super().__init__(f"La respuesta introducida no es válida")


@typechecked
class Question:
    def __init__(self, question_name: str, statement: str, possible_answer: list[tuple[str, float]],
                 base_score: int = 1):
        self.__question_name = question_name
        self.__statement = statement
        self.__posible_answer = possible_answer
        self.__base_score = base_score

    @property
    def question_name(self):
        return self.__question_name

    @property
    def statement(self):
        return self.__statement

    @property
    def posible_answer(self):
        return self.__posible_answer.copy()

    @property
    def base_score(self):
        return self.__base_score

    def get_score(self, user_answer: int):
        if user_answer < 1 or user_answer > len(self.__posible_answer):
            raise QuestionError
        score = self.__posible_answer[user_answer - 1][1]  # -1 porque el el index empieza en 0
        return score
