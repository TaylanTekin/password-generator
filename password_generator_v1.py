import random
import string
import os

def save_password(password):
    with open("password.txt", "a") as f:
        f.write(password + "\n")

def show_saved_password():
    if not os.path.exists("password.txt"):
        print("No passwords saved yet")   
        return
    with open("password.txt", "r") as f:
        
def check_strength(password)



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
            print("Uppercase letters included")
        elif uppercase == "n":
                
            print("Uppercase letters not included")
        else:
            print("Please choose (y/n)")
            input("Press Enter to continue")
            continue
                
        lowercase = input("Include lowercase letters? (y/n): ").strip().lower()
        if lowercase == "y":
            all_chars += string.ascii_lowercase
            print("Lowercase letters included")
        elif lowercase == "n":
                
            print("Lowercase letters not included")
        else:
            print("Please choose (y/n)")
            input("Press Enter to continue")
            continue
                
        numbers = input("Include numbers? (y/n): ").strip().lower()
        if numbers == "y":
            all_chars += string.digits
            print("Numbers included")
        elif numbers == "n":
            
            print("Numbers not included")
        else:
            print("Please choose (y/n)")
            input("Press Enter to continue")
            continue
                
        symbols = input("Include symbols? (y/n): ").strip().lower()
        if symbols == "y":
            all_chars += string.punctuation
            print("Symbols included")
        elif symbols == "n":
            
            print("Symbols not included")
        else:
            print("Please choose (y/n)")
            input("Press Enter to continue")
            continue

        if all_chars == "":
            print("You must select at least one character type!")
            input("Press Enter to restart")
            continue

        password = "".join(random.choice(all_chars) for _ in range(length))
        print(f"Generated password: {password}")
        strength = check_strength(password)
        print(f"Password strength: {strength}")

        save = input("Do you want to save this password? (y/n): ")
        if save.lower() == "y":
            save_password(password)
            print("password saved to file")
        
        again = input("Generate another password? (y/n): ")
        if again != "y":
            print("Thanks for using Password generator")
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