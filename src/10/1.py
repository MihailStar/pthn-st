# 1
from typing import Any, List, TypeVar

T = TypeVar("T")


def sum_of_list(values: List[T]) -> float:
    accumulator = 0.0

    for value in values:
        try:
            numeric_val = float(value)
            accumulator += numeric_val

        except ValueError as value_exception:
            print("ValueError:", value_exception)

        except TypeError as type_exception:
            print("TypeError:", type_exception)

    return accumulator


list1 = [1, 2, 3]
list2 = ["1", 2.5, "3.0"]
list3 = ["", "1"]
list4 = []
list5 = ["John", "Doe", "was", "here"]
nasty_list: List[KeyError | dict[Any, Any] | list[Any]] = [KeyError(), [], dict()]

assert sum_of_list(list1) == 6
assert sum_of_list(list2) == 6.5
assert sum_of_list(list3) == 1  # -> 'ValueError: ...'
assert sum_of_list(list4) == 0
assert sum_of_list(list5) == 0  # -> 'ValueError: ...'
assert sum_of_list(nasty_list) == 0  # -> 'TypeError: ...'


# 2
class TooLongString(Exception):
    pass


def verify_short_string(string: str) -> None:
    """raise `TooLongString`"""

    if len(string.replace(" ", "")) >= 10:
        raise TooLongString()


verify_short_string("short")

verify_short_string("10   chars")

try:
    verify_short_string("this is long")

except TooLongString as exception:
    print("Все ок! Исключение обработалось")  # -> 'Все ок! Исключение обработалось'
    pass

else:
    print("Исключение не обработалось :(\nИщите ошибку")
    assert False
