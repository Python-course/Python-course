"""
**Задание 2.2. Разворот предложения по словам**

Запросить у пользователя предложение без знаков препинания и вывести строку с обращённым порядком слов.

Пример работы::

    Введите предложение: Завтра идем купаться
    Разворот по словам: Купаться идем завтра
"""


def reverse_sentence(sentence: str) -> str:
    """
    Обращает порядок слов в предложении без знаков препинания.

    :param sentence: Предложение.
    :return: Результат преобразования.
    """
    return " ".join(sentence.split()[::-1]).capitalize()


if __name__ == "__main__":
    sentence = input("Введите предложение: ")
    print(f"Разворот по словам: {reverse_sentence(sentence)}")
