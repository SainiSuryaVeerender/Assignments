class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Brand: {self.brand}, Year: {self.year}, Number of Doors: {self.number_of_doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"Brand: {self.brand}, Year: {self.year}, Has Sidecar: {self.has_sidecar}"

def main():
    vehicle_type = input("Enter vehicle type (Car/Motorcycle): ").strip().lower()
    brand = input("Enter the brand of the vehicle: ")
    year = input("Enter the year of the vehicle: ")

    if vehicle_type == 'car':
        number_of_doors = int(input("Enter the number of doors: "))
        vehicle = Car(brand, year, number_of_doors)
    elif vehicle_type == 'motorcycle':
        has_sidecar = input("Does it have a sidecar? (yes/no): ").strip().lower() == 'yes'
        vehicle = Motorcycle(brand, year, has_sidecar)
    else:
        print("Invalid vehicle type.")
        return

    print(vehicle.get_info())

if __name__ == "__main__":
    main()






from abc import ABC, abstractmethod

# Define the abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Define the Dog class
class Dog(Animal):
    def make_sound(self):
        return "Woof"

# Define the Cat class
class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Define the Cow class
class Cow(Animal):
    def make_sound(self):
        return "Moo"

# Function to play the sound of the animal
def play_sound(animal: Animal):
    print(animal.make_sound())

# Main function to take user input
def main():
    animal_input = input("Enter an animal (dog, cat, cow): ").strip().lower()

    if animal_input == "dog":
        animal = Dog()
    elif animal_input == "cat":
        animal = Cat()
    elif animal_input == "cow":
        animal = Cow()
    else:
        print("Invalid animal. Please enter dog, cat, or cow.")
        return

    play_sound(animal)

# Example usage
if __name__ == "__main__":
    main()




from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self):
        self._balance = 0  

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if self._balance - amount < 500:
            print("Withdrawal denied: Cannot withdraw below $500 balance.")
        else:
            self._balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def get_balance(self):
        return self._balance

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if self._balance - amount < -1000:
            print("Withdrawal denied: Overdraft limit exceeded.")
        else:
            self._balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def get_balance(self):
        return self._balance

def main():
    account_type = input("Choose account type (savings or current): ").strip().lower()
    if account_type == "savings":
        account = SavingsAccount()
    elif account_type == "current":
        account = CurrentAccount()
    else:
        print("Invalid account type. Please choose savings or current.")
        return

    while True:
        action = input("Would you like to deposit, withdraw, or check balance? (type 'exit' to quit): ").strip().lower()
        
        if action == "deposit":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif action == "withdraw":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif action == "check balance":
            print(f"Current balance: ${account.get_balance():.2f}")
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()








class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def get_salary(self):
        return self.salary

    def increase_salary(self, percent):
        increase_amount = (self.salary * percent) / 100
        self.salary += increase_amount
        print(f"New Salary for {self.name}: {self.salary:.2f}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Programming Language: {self.programming_language}"

def create_employee():
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    return name, salary

def create_manager():
    name, salary = create_employee()
    department = input("Enter department: ")
    return Manager(name, salary, department)

def create_developer():
    name, salary = create_employee()
    programming_language = input("Enter programming language: ")
    return Developer(name, salary, programming_language)

def main():
    employees = []

    while True:
        employee_type = input("Enter '1' for Manager, '2' for Developer, or 'q' to quit: ")
        if employee_type == '1':
            employees.append(create_manager())
        elif employee_type == '2':
            employees.append(create_developer())
        elif employee_type == 'q':
            break
        else:
            print("Invalid input. Please try again.")

    for emp in employees:
        print(emp.get_details())

    for emp in employees:
        percent = float(input(f"Enter salary increase percentage for {emp.name}: "))
        emp.increase_salary(percent)

if __name__ == "__main__":
    main()




from abc import ABC, abstractmethod

class Media(ABC):
    @abstractmethod
    def play(self):
        pass

class Audio(Media):
    def __init__(self, file_name):
        self.file_name = file_name

    def play(self):
        print(f"Playing audio file: {self.file_name}")

class Video(Media):
    def __init__(self, file_name):
        self.file_name = file_name

    def play(self):
        print(f"Playing video file: {self.file_name}")

class LiveStream(Media):
    def __init__(self, stream_url):
        self.stream_url = stream_url

    def play(self):
        print(f"Playing live stream from: {self.stream_url}")

def start_media(media):
    media.play()

def main():
    media_objects = []

    while True:
        media_type = input("Enter '1' for Audio, '2' for Video, '3' for Live Stream, or 'q' to quit: ")
        if media_type == '1':
            file_name = input("Enter the .mp3 file name: ")
            media_objects.append(Audio(file_name))
        elif media_type == '2':
            file_name = input("Enter the .mp4 file name: ")
            media_objects.append(Video(file_name))
        elif media_type == '3':
            stream_url = input("Enter the live stream URL: ")
            media_objects.append(LiveStream(stream_url))
        elif media_type == 'q':
            break
        else:
            print("Invalid input. Please try again.")

    for media in media_objects:
        start_media(media)

if __name__ == "__main__":
    main()





from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, num_copies):
        self.title = title
        self.author = author
        self.num_copies = num_copies
        self.is_borrowed = False

    def borrow(self):
        if self.num_copies > 0:
            self.num_copies -= 1
            self.is_borrowed = True
            print(f"You have borrowed the book: {self.title} by {self.author}.")
        else:
            print("Sorry, this book is currently unavailable.")

    def return_item(self):
        self.num_copies += 1
        self.is_borrowed = False
        print(f"You have returned the book: {self.title}.")

class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed the DVD: {self.title} directed by {self.director}.")
        else:
            print("Sorry, this DVD is currently unavailable.")

    def return_item(self):
        self.is_borrowed = False
        print(f"You have returned the DVD: {self.title}.")

def borrow_item(item):
    item.borrow()

def main():
    
    book1 = Book("2002", "melfred hens", 3)
    dvd1 = DVD("psychology of money", "kael william", 506)

    user_choice = input("Do you want to borrow a book or a DVD? (book/dvd): ").strip().lower()

    if user_choice == "book":
        borrow_item(book1)
    elif user_choice == "dvd":
        borrow_item(dvd1)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()


