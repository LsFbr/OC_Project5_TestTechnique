# Écrivez votre code ici !
class Person:
    # Initialisation des attributs
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Méthode pour afficher les détails de la personne
    def display_details(self):
        print(f"\nNom: {self.name}\nÂge: {self.age}")


# Classe Employee qui hérite de la classe Person
class Employee(Person):
    # Initialisation des attributs
    # en appelant la méthode __init__ de la classe mère
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    # Méthode pour afficher les détails de l'employé
    # en appelant la méthode display_details de la classe mère
    def display_details(self):
        super().display_details()
        print(f"Salaire: {self.salary}")


# Test
employee = Employee("David Douillet", 30, 50000)
employee.display_details()

person = Person("Davide Douillette", 25)
person.display_details()
