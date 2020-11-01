people = [
    {"name": "melika", "house": "az"},
    {"name": "amir", "house": "mashhad"},
    {"name": "sina", "house": "torento"}
]

# def f(person):
#     return person["house"]
# people.sort(key=f)

people.sort(key=lambda person: person["name"])
print(people)