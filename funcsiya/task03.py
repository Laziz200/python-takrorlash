def filter_people(people):
    result = []
    for person in people:
        if person["age"] > 18 and person["cars"] > 1:
            result.append(person)
    return result

people = [
    {"Name": "Asil", "age": 9, "cars": 3},
    {"Name": "Laziz", "age": 19, "cars": 2},
    {"Name": "Sardor", "age": 25, "cars": 7},
    {"Name": "Og`abek", "age": 5, "cars": 5},
]

filtered_people = filter_people(people)
for person in filtered_people:
    print(person)