def defa(name, age, gender,) -> dict:
    person = {
        'name': name,
        'age': age,
        'gender': gender,
    }
    return person

person = defa("Daneel", 25, "male")

print(person)

def defaa(name, age, gender,) -> dict:
    persona = {
        'name': name,
        'age': age,
        'gender': gender,
    }
    return persona

persona = defa("Vlad", 24, "male")
for key in persona.keys():
    print(f"{key}:{persona[key]}")