import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length > 0:
            generated_password = generate_password(length)
            print(f"\nGenerated Password: {generated_password}")
        else:
            print("Invalid length. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("Welcome to the Password Generator!\n")
    password_generator()
