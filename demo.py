import random

def main():
    print("Welcome to the Innonation Day!")
    print_random_number()
    name = "Alice"
    print(greet(name))




def greet(name):
    return f"Hello, {name}!"
def print_random_number():
    print(generate_random_number())

def generate_random_number():
    return random.randint(1, 100)

if __name__ == "__main__":
    main()