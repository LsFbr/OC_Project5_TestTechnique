# Écrivez votre code ici !
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"\nNom: {self.name}\nÂge: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Salaire: {self.salary}")


employee = Employee("David Douillet", 30, 50000)
employee.display_details()

person = Person("Davide Douillette", 25)
person.display_details()
