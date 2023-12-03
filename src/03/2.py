# 1
original = " Python strings are COOL! "
lower_cased = original.lower()
stripped = original.strip()

stripped_lower_cased = original.strip().lower()

assert lower_cased == " python strings are cool! "
assert stripped == "Python strings are COOL!"
assert stripped_lower_cased == "python strings are cool!"


# 2
ugly = " tiTle of MY new Book\n\n"

pretty = ugly.strip().title()

print("pretty: {}".format(pretty))  # -> 'pretty: Title Of My New Book'
assert pretty == "Title Of My New Book"


# 3
verb = "is"
language = "Python"
punctuation = "!"

sentence = "Learning {} {} fun{}".format(language, verb, punctuation)

print("sentence: {}".format(sentence))  # -> 'sentence: Learning Python is fun!'
assert sentence == "Learning Python is fun!"
