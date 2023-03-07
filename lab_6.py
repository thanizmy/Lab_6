
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

# FIXME: decodes passwords


if __name__ == "__main__":
    while True:
        user_input = menu()
        if user_input == 1:
            user_password = input("Please enter your password to encode: ")
            print("Your password has been encoded and restored!")
            print()
            new_password = encode_password(user_password)
        elif user_input == 2:   # FIXME: Encodes passwords
            pass
        else:
            break

