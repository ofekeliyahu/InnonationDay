import random
def main():
    print("Welcome")

def generate_random_number():
    return random.randint(1, 100)

def print_random_number():
    print(generate_random_number())

if __name__ == "__main__":
    main()
    print_random_number()