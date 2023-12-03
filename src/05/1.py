# 1
from typing import List


def count_even_numbers(numbers: List[int]) -> int:
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count


assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3
assert count_even_numbers([1, 3, 5, 7]) == 0
assert count_even_numbers([-2, 2, -10, 8]) == 4


# 2
WANTED_PEOPLE = ["John Doe", "Clint Eastwood", "Chuck Norris"]


def find_wanted_people(people_to_check: List[str]) -> List[str]:
    result: List[str] = []

    for people in people_to_check:
        if people in WANTED_PEOPLE:
            result.append(people)

    return result


people_to_check1 = ["Donald Duck", "Clint Eastwood", "John Doe", "Barack Obama"]
wanted1 = find_wanted_people(people_to_check1)
assert len(wanted1) == 2
assert "John Doe" in wanted1
assert "Clint Eastwood" in wanted1

people_to_check2 = ["Donald Duck", "Mickey Mouse", "Zorro", "Superman", "Robin Hood"]
wanted2 = find_wanted_people(people_to_check2)
assert wanted2 == []


# 3
def average_length_of_words(string: str) -> float:
    words = string.split(" ")
    word_lengths = list(map(lambda word: len(word), words))
    result = round(sum(word_lengths) / len(word_lengths), 1)

    return result


assert average_length_of_words("only four lett erwo rdss") == 4
assert average_length_of_words("one two three") == 3.7
assert average_length_of_words("one two three four") == 3.8
assert average_length_of_words("") == 0
