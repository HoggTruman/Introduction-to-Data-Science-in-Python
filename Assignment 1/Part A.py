import re


def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    return re.findall(r'[A-Z][a-z]*', simple_string)

print(names())
assert len(names()) == 4, "There are four names in the simple_string"