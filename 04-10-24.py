#### Single Inheritance
#####   Create a base class Animal with an attribute name and a method speak().

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

my_dog = Dog("Buddy")

my_dog.speak()


#####  Multiple Inheritance
###  Create a class Teacher with an attribute subject. Then, create a class Researcher with an attribute field.
class Teacher:
    def __init__(self, subject):
        self.subject = subject


class Researcher:
    def __init__(self, field):
        self.field = field

class TeachingResearcher(Teacher, Researcher):
    def __init__(self, subject, field):
        Teacher.__init__(self, subject)
        Researcher.__init__(self, field)
    
    def display(self):
        print(f"Subject: {self.subject}, Field: {self.field}")

teaching_researcher = TeachingResearcher("Mathematics", "Trigonometry")
teaching_researcher.display()


#### Create two base classes: Bird and Flyable.

class Bird:
    def __init__(self, species):
        self.species = species

class Flyable:
    def fly(self):
        print("Flying")

class Eagle(Bird, Flyable):
    def display(self):
        print(f"Species: {self.species}")
        self.fly()

eagle = Eagle("Bold Eagle")

eagle.display()




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_info(self):
        person_info = super().display_info()
        return f"{person_info}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display_info(self):
        employee_info = super().display_info()
        return f"{employee_info}, Department: {self.department}"

manager = Manager("SURYA", 24, 80000, "DEVELOPER")
print(manager.display_info())




###### Hierarchical Inheritance


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_details(self):
        return f"{super().display_details()}, Programming Language: {self.programming_language}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display_details(self):
        return f"{super().display_details()}, Team Size: {self.team_size}"


class Intern(Developer):
    def __init__(self, name, salary, programming_language, internship_duration):
        super().__init__(name, salary, programming_language)
        self.internship_duration = internship_duration

    def display_details(self):
     return f"{super().display_details()}, Internship Duration: {self.internship_duration} months"
    


   
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, Number of Doors: {self.num_doors}"


class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def display_info(self):
        return f"{super().display_info()}, Type: {self.bike_type}"

my_car = Car("Toyota", "HYCROSS", 4)
my_bike = Bike("Bajaj Pulsar", "NS 250", "Sport")

print(my_car.display_info())
print(my_bike.display_info())



###### Hybrid Inheritance

class Device:
    def __init__(self, name):
        self.name = name

class Phone(Device):
    def __init__(self, name, phone_number):
        super().__init__(name)
        self.phone_number = phone_number

class Tablet(Device):
    def __init__(self, name, screen_size):
        super().__init__(name)
        self.screen_size = screen_size

class Smartphone(Phone, Tablet):
    def __init__(self, name, phone_number, screen_size, os):
        Phone.__init__(self, name, phone_number)
        Tablet.__init__(self, name, screen_size)
        self.os = os

    def display_info(self):
        print(f"Smartphone Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Screen Size: {self.screen_size}")
        print(f"Operating System: {self.os}")

my_smartphone = Smartphone("Galaxy S21", "123-456-7890", "6.2 inches", "Android")

my_smartphone.display_info()




#####  Basic Inheritance



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  
        self.grade = grade

    def display_info(self):
    
        super().display_info()
        print(f"Grade: {self.grade}")



person1 = Person("ABHI RAM", 40)
person1.display_info()


student1 = Student("MADHAV", 30, "A")
student1.display_info()