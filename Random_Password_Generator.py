import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters 
    if use_numbers:
        characters += string.digits  
    if use_symbols:
        characters += string.punctuation  

    if not characters:
        print("Error: No character types selected!")
        return None

    return "".join(random.choice(characters) for _ in range(length))

def get_user_input():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Error: Length must be a positive number.")
            return None

        use_letters = input("Include letters? (yes/no): ").lower() == "yes"
        use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
        use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print("\nGenerated Password:", password)
    except ValueError:
        print("Error: Please enter a valid number for length.")

get_user_input()
