
# Prints menu screen
def menu():
    print("Menu",
          "-------------",
          "1. Encode",
          "2. Decode",
          "3. Quit", sep="\n")
    print()
    option = int(input("Please enter an option: "))
    return option


# Encodes passwords
def encode_password(string):
    password = ""
    for number in string:
        int_number = int(number)
        password += str(int_number + 3) if int_number < 7 else str(int_number - 7)
    return password


# Decodes passwords
def decode_password(string):
    password = ""
    for number in string:
        int_number = int(number)
        password += str(int_number - 3) if int_number > 2 else str(int_number + 7)
    return password


if __name__ == "__main__":
    while True:
        user_input = menu()
        if user_input == 1:
            user_password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            print()
            new_password = encode_password(user_password)
        elif user_input == 2:
            old_password = decode_password(new_password)
            print(f"The encoded password is {new_password}, and the original password is {old_password}. ")
            print()
        else:
            break
