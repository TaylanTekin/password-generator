import random
import string
import os

def save_password(password):
    with open("password.txt", "a") as f:
        f.write(password + "\n")

def show_saved_passwords():
    if not os.path.exists("password.txt"):
        print("No passwords saved yet.")
        return
    with open("password.txt", "r") as f:
        print("Saved passwords and their strength:")
        for line in f:
            pw = line.strip()
            print(f"{pw} - Strength: {check_strength(pw)}")

def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 6 or score <= 1:
        return "Weak"
    elif length >= 6 and score == 2:
        return "Medium"
    elif length >= 8 and score >= 3:
        return "Strong"
    else:
        return "Medium"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Password Generator")
    print("1. Generate password")
    print("2. Show saved passwords")
    print("3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            try:
                length = int(input("How long should the password be?: "))
            except ValueError:
                print("Please enter a valid number.")
                input("Press Enter to continue...")
                continue

            all_chars = ""

            uppercase = input("Include uppercase letters? (y/n): ").strip().lower()
            if uppercase == "y":
                all_chars += string.ascii_uppercase
            elif uppercase != "n":
                print("Invalid choice")
                continue

            lowercase = input("Include lowercase letters? (y/n): ").strip().lower()
            if lowercase == "y":
                all_chars += string.ascii_lowercase
            elif lowercase != "n":
                print("Invalid choice")
                continue

            numbers = input("Include numbers? (y/n): ").strip().lower()
            if numbers == "y":
                all_chars += string.digits
            elif numbers != "n":
                print("Invalid choice")
                continue

            symbols = input("Include symbols? (y/n): ").strip().lower()
            if symbols == "y":
                all_chars += string.punctuation
            elif symbols != "n":
                print("Invalid choice")
                continue

            if all_chars == "":
                print("You must select at least one character type!")
                input("Press Enter to restart")
                continue

            password = "".join(random.choice(all_chars) for _ in range(length))
            print(f"Generated password: {password}")
            strength = check_strength(password)
            print(f"Password strength: {strength}")

            save = input("Do you want to save this password? (y/n): ").strip().lower()
            if save == "y":
                save_password(password)
                print("Password saved to file")

            again = input("Generate another password? (y/n): ").strip().lower()
            if again != "y":
                break

    elif choice == "2":
        show_saved_passwords()
        input("Press Enter to continue...")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
        input("Press Enter to continue...")
