# 1
class Calculator:
    number_a: int
    number_b: int

    def __init__(self, number_a: int, number_b: int) -> None:
        self.number_a = number_a
        self.number_b = number_b

    def calculate_power(self) -> int:
        return self.number_a**self.number_b

    def calculate_sum(self, number_c: int) -> int:
        return self.number_a + self.number_b + number_c


calc = Calculator(2, 3)
assert calc.calculate_power() == 8
assert calc.calculate_sum(4) == 9


# 2
from typing import Final, Literal


class StringManipulator:
    """Docstring of StringManipulator"""

    category: Final[Literal["Manipulator"]] = "Manipulator"
    phrase: str

    def __init__(self, original: str) -> None:
        self.phrase = original

    def reverse_words(self) -> None:
        self.phrase = " ".join(reversed(self.phrase.split(" ")))

    def make_title(self) -> None:
        self.phrase = " ".join(
            map(lambda word: word.title(), reversed(self.phrase.split(" ")))
        )

    def get_manipulated(self) -> str:
        return self.phrase


assert StringManipulator.__doc__ == "Docstring of StringManipulator"
assert StringManipulator.category == "Manipulator"

str_manip = StringManipulator("cOOL pyThON")
str_manip.reverse_words()
assert str_manip.get_manipulated() == "pyThON cOOL"

str_manip = StringManipulator("cOOL pyThON")
str_manip.make_title()
assert str_manip.get_manipulated() == "Python Cool"


# 3
from enum import Enum


class Energy(Enum):
    MIN = 0
    MAX = 10


class Dog:
    _energy: int

    def __init__(self) -> None:
        self._energy = Energy.MAX.value

    def get_energy(self) -> int:
        return self._energy

    def bark(self) -> None:
        if self._energy == Energy.MIN.value:
            return

        self._energy -= 1
        print("Gav!")

    def sleep(self) -> None:
        if self._energy == Energy.MAX.value:
            return

        self._energy += 2


doge = Dog()
assert doge.get_energy() == 10

doge.bark()  # -> 'Gav!'
doge.bark()  # -> 'Gav!'
doge.bark()  # -> 'Gav!'
assert doge.get_energy() == 7

doge.sleep()
assert doge.get_energy() == 9

another_doge = Dog()
assert another_doge.get_energy() == 10
