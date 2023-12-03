# 1
from typing import List

words: List[str] = ["PYTHON", "JOHN", "chEEse", "hAm", "DOE", "123"]
upper_case_words: List[str] = []

for word in words:
    if word.isupper():
        upper_case_words.append(word)

print(upper_case_words)  # -> ['PYTHON', 'JOHN', 'DOE']

assert upper_case_words == ["PYTHON", "JOHN", "DOE"]


# 2
magic_dict = dict(val1=44, val2="secret value", val3=55.0, val4=1)

sum_of_values = 0

for value in magic_dict.values():
    if isinstance(value, (int, float)):
        sum_of_values += value

print(sum_of_values)  # -> 100.0

assert sum_of_values == 100


# 3
numbers: List[int] = [1, 3, 4, 6, 81, 80, 100, 95]

my_list: list[str] = []

for number in numbers:
    if number % 5 == 0:
        if number % 2 == 0:
            my_list.append("five even")
        else:
            my_list.append("five odd")
    elif number % 2 == 0:
        my_list.append("even")
    else:
        my_list.append("odd")

assert my_list == [
    "odd",
    "odd",
    "even",
    "even",
    "odd",
    "five even",
    "five even",
    "five odd",
]
