import ast


f = open("p022_names.txt","r")
contents = f.read()
f.close()

names_string = "[" + contents + "]"
names = ast.literal_eval(names_string)
names.sort()


def alphabetical_value(name):
    score = 0
    for i in range(0, len(name)):
        score += ord(name[i]) - 64
    return score


def solution():
    scores = 0
    for i in range(0, len(names)):
        scores += (i + 1) * alphabetical_value(names[i])
    return scores


assert alphabetical_value("COLIN") == 53

print(solution())
