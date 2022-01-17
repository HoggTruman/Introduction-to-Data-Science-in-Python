import re
def logs():
    with open("logdata.txt", "r") as file:
        result = []
        for line in file:
            items = re.findall(r'(^\S*) - (\S*) \[(.*)] "(.*)"', line)[0]
            result.append({"host": items[0],
                           "user_name": items[1],
                           "time": items[2],
                           "request": items[3]
                           })
    return result


# print(logs())