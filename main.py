password = ""
encoded_password = ""
def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


#adds 3 to each digit and concatenates it back into a string and saves the variable globally
def encode():
    global password
    global encoded_password
    password = (input("Please enter your password to encode:"))
    print("Your password has been encoded and stored!")

    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password

#prints both the encoded password and the original password



if __name__ == "__main__":
    while True:
        menu()
        user_input = input("Please enter an option:")

#each menu item and appropriate function below
        if user_input == "1":
            encode()
        if user_input == "2":
            decode(password)
        if user_input == "3":
            quit()


