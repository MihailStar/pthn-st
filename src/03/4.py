# 1
my_list = []

my_list.append("Python")
my_list.append("is ok")
my_list.append("sometimes")
print(my_list)  # -> ['Python', 'is ok', 'sometimes']

my_list.remove("sometimes")
print(my_list)  # -> ['Python', 'is ok']

my_list[2 - 1] = "is neat"
print(my_list)  # -> ['Python', 'is neat']

assert my_list == ["Python", "is neat"]


# 2
original = ["I", "am", "learning", "hacking", "in"]

# modified = list(original)
# modified = original.copy()
# modified = [*original]
modified = original[:]
modified[3] = "lists"
modified.append("Python")

assert original == ["I", "am", "learning", "hacking", "in"]
assert modified == ["I", "am", "learning", "lists", "in", "Python"]


# 3
list1 = [6, 12, 5]
list2 = [6.2, 0, 14, 1]
list3 = [0.9]

# my_list = [*list1, *list2, *list3]
# my_list = list1 + list2 + list3
# my_list.sort(reverse=True)
my_list = sorted(list1 + list2 + list3, reverse=True)

print(my_list)  # -> [14, 12, 6.2, 6, 5, 1, 0.9, 0]
assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]
