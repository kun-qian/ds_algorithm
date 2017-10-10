def josephus(n, a):

    persons = list(range(n))
    while len(persons) > 2:
        for i in range(a - 1):
            persons.append(persons.pop(0))
        persons.pop(0)
    return [x + 1 for x in persons]


print(josephus(41, 3))
