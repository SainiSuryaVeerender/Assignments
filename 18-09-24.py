
#### create a list to Dmart store products and their prices based on user input then calculate the total price of all the products
def product_price_list():
    products = []
    total_price = 0

    num_products = int(input("Enter the number of products: "))

    for i in range(num_products):
        product_name = input(f"Enter the name of product {i + 1}: ")
        product_price = float(input(f"Enter the price of {product_name}: "))
        
        products.append((product_name, product_price))
        total_price += product_price

    print("\nProducts and Prices:")
    for product in products:
        print(f"{product[0]}: ${product[1]:.2f}")

    print(f"\nTotal Price: ${total_price:.2f}")

if __name__ == "__main__":
    product_price_list()







####### Guessing game
import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (1-100): "))
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
