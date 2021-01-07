def adults(people):
    return [person['name'] for person in people if person['age'] > 18]


ppl = [
    {"name": 'Khalid Robinson', "age": 22},
    {"name": 'Ariel Winter', "age": 20},
    {"name": 'Post Malone', "age": 25},
    {"name": 'Willow Smith', "age": 17}
]

print(adults(ppl))
