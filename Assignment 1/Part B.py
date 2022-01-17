import re
def grades():
    with open("grades.txt", "r") as file:
        grades = file.read().split('\n')

    return [re.findall(r'^[A-Za-z ]*', student)[0] for student in grades if student[-1] == 'B']


print(grades())