

class Student:

    def __init__(self, params):
        self.name = params.get("name")
        self.age = params.get("age")
        self.combo = params.get("combo")


def make_student(*args):
    student = Student(args)
    return student


ignat = {"name": "Ignat", "age": 27, "combo": "Kayote"}
animal = Student(ignat)

print(animal.name)
