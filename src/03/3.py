# 1
first_name = "John"
last_name = "Doe"
favorite_hobby = "Python"
sports_hobby = "gym"
age = 82

my_dict = {"name": f"{first_name} {last_name}", "age": age}
my_dict["hobbies"] = [favorite_hobby, sports_hobby]

assert my_dict == {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}


# 2
dict1 = dict(key1="This is not that hard", key2="Python is still cool")
dict2 = {"key1": 123, "special_key": "secret"}
dict3 = dict([("key2", 456), ("keyX", "X")])

# my_dict = {}
# my_dict.update(dict1)
# my_dict.update(dict2)
# my_dict.update(dict3)
# my_dict = {**dict1, **dict2, **dict3}
my_dict = dict1 | dict2 | dict3
special_value = my_dict["special_key"]
del my_dict["special_key"]

assert my_dict == {"key1": 123, "key2": 456, "keyX": "X"}
assert special_value == "secret"

assert dict1 == {"key1": "This is not that hard", "key2": "Python is still cool"}
assert dict2 == {"key1": 123, "special_key": "secret"}
assert dict3 == {"key2": 456, "keyX": "X"}
