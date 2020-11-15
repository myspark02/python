class Math :
    @staticmethod # means that this method dosen't access anything
    def add5(num) :
        return num+5

    @staticmethod
    def pr() :
        print("run")

print(Math.add5(10))
Math.pr()

class Person :
    number_of_people = 0

    def __init__(self, name) :
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()

    @classmethod
    def get_number_of_people(cls) :
        return cls.number_of_people

    @classmethod
    def add_person(cls) :
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")

print(Person.get_number_of_people())

class Pet:
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def show(self) :
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self) :
        print("I don't know what to say")


class Cat(Pet) :
    def __init__(self, name, age, color) :
        super().__init__(name, age)
        self.color = color

    def speak(self) :
        print("Meow")

    def show(self) :
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet) :
    def speak(self) :
        print("Bark")

p = Pet("Time", 19)
p.speak()

c = Cat("Bill", 24, "Brown")
c.speak()
c.show()