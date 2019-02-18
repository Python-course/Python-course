"""
**Задание 3.5. Симметричная троичная система счисления**

В симметричной троичной системе счисления имеется три цифры: ``-1``, ``0``, ``1``.
Для упрощеня будем отображат их знаками ``{-, 0, +}``.
Основание системы равно ``3`` и преобразование в десятичную систему счисления происходит по простому правилу:
нужно взять сумму цифр умноженных на степень основания позиции.

``-0+ = -1 * 3^2 + 0 * 3^1 + 1 * 3^0 = -9 + 0 + 1 = -8``

Нужно написать функцию преобразования целого дестичного числа в симметричную троичную систему счисления.

Таблица для проверки результатов:

.. csv-table::
   :header: "Десятичная с.с.", "Троичная с.с."

   ``-5``, ``-++``
   ``-4``,  ``--``
   ``-3``,  ``-0``
   ``-2``,  ``-+``
   ``-1``,   ``-``
    ``0``,   ``0``
    ``1``,   ``+``
    ``2``,  ``+-``
    ``3``,  ``+0``
    ``4``,  ``++``
    ``5``, ``+--``
    ``6``, ``+-0``
    ``7``, ``+-+``
    ``8``, ``+0-``
    ``9``, ``+00``
   ``10``, ``+0+``
   ``11``, ``++-``
   ``12``, ``++0``
"""

from itertools import product

# Словарь для преобразования троичных цифр в десятичные.
symmetric_ternary_numbers = {"-": -1, "0": 0, "+": +1}


def to_symmetric_ternary_number(decimal: int) -> str:
    """
    Преобразует число из десятичной системы счисления в симметричную троичную.

    :param decimal: Десятичное число.
    :return: Троичное число.
    """

    # Количество цифр в для перебора.
    size = 1

    while True:
        # Находим троичное число полным перебором.
        ternary_number = list(filter(
            lambda x: from_symmetric_ternary_number(x) == decimal,
            ["".join(x) for x in product("".join(symmetric_ternary_numbers.keys()), repeat=size)]
        ))

        if len(ternary_number) == 0:
            size += 1
        else:
            return ternary_number[0]


def from_symmetric_ternary_number(ternary_number: str) -> int:
    """
    Преобразует число из симметричной троичной системы счисления в десятичную.

    :param ternary_number: Троичное число.
    :return: Десятичное число.
    """

    return sum([symmetric_ternary_numbers[ternary_number[::-1][i]] * 3 ** i for i in range(len(ternary_number))[::-1]])


if __name__ == "__main__":
    decimal = int(input("Введите десятичное число: "))

    print(f"Троичное число: {to_symmetric_ternary_number(decimal)}")