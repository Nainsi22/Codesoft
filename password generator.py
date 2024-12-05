import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ' '.join(random.choice(characters) for __ in range(length))
    return password
def main():
    print("Welcome to the password generator!")
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("password length should be at least 6 characters!")
        else:
            password = generate_password(length)
            print(f"Your generated password is:{password}")
    except ValueError:
        print("Invalid input! please enter a valid number:")
if __name__ =="__main__":
    main()
