import os

dir_script = os.getcwd()

data_folder = "data_file_io_exercise"
data_file_1 = "numbers.txt"
data_file_2 = "simple_file.txt"
data_file_3 = "simple_file_with_empty_lines.txt"

dir_path = os.path.join(dir_script, data_folder)
file_1_path = os.path.join(dir_path, data_file_1)
file_2_path = os.path.join(dir_path, data_file_2)
file_3_path = os.path.join(dir_path, data_file_3)

print(dir_path)

file_1_input_string = """1
2.5
16
4
5
12
15
16
18
100"""

file_2_input_string = """First line
Second line
Third
And so the story goes!"""

file_3_input_string = """The Title of the Story

First paragraph with some
nonsense words.

Then we move to second paragraph and so on."""

os.makedirs(dir_path, exist_ok=True)

with open(file_1_path, "w") as f:
    f.write(file_1_input_string)

with open(file_2_path, "w") as f:
    f.write(file_2_input_string)

with open(file_3_path, "w") as f:
    f.write(file_3_input_string)


# 1
def sum_numbers_in_file(input_file: str) -> float:
    total = 0.0

    with open(input_file, "r") as f:
        for line in f:
            line_stripped = line.strip()
            total += float(line_stripped)

    return total


assert sum_numbers_in_file(file_1_path) == 189.5


# 2
def find_first_words(path: str) -> list[str]:
    first_words: list[str] = []

    with open(path, "r") as f:
        for line in f:
            first_words.append(line.split()[0] if line.strip() else "")

    return first_words


expected_file_1 = ["First", "Second", "Third", "And"]
assert find_first_words(file_2_path) == expected_file_1

expected_file_2 = ["The", "", "First", "nonsense", "", "Then"]
assert find_first_words(file_3_path) == expected_file_2

os.remove(file_1_path)
os.remove(file_2_path)
os.remove(file_3_path)
os.removedirs(dir_path)
