import re as regexp

# 1
pattern_1 = regexp.compile(r"cat")

result_1 = pattern_1.search("CatcatCATCaT")

if result_1 is None:
    raise Exception("Not Found")

assert result_1.start() == 3
assert result_1.end() == 6
assert result_1.group(0) == "cat"


# 2
pattern_2 = regexp.compile(r"ab{2,3}")

result_2 = pattern_2.findall("Ab")
result_3 = pattern_2.findall("Cgiabb_abbb_ab_abbbbb")

assert result_2 == []

assert result_3 == ["abb", "abbb", "abbb"]


# 3
pattern_3 = regexp.compile(r"[a-z]+_[a-z]+")

result_4 = pattern_3.search("John_Smith name_surname_Name_Surname")
result_5 = pattern_3.search("John_Smith_name_surname_Name_Surname")

if result_4 is None or result_5 is None:
    raise Exception("Not Found")

assert result_4.group(0) == "name_surname"
assert result_5.group(0) == "mith_name"
