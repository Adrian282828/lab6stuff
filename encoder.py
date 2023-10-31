def encode(password):
    # Creates the empty encoded password
    encoded_pass = ''

    # Takes the un-coded password from the function parameter and forces it to be a string no matter the input
    string_password = str(password)

    for element in string_password:
        # force each string number of the password to be an integer type.
        # Then use the addition and modulo to implement the shift and encode operations respectively.
        temp = str((int(element) + 3) % 9)

        # tack on the coded numbers to the string
        encoded_pass += temp

    return encoded_pass


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def decode(encoded_password):
    # Creates the empty decoded password
    decoded_password = ''

    for element in encoded_password:
        # force each string number of the encoded password to be an integer type.
        # Then use the subtraction and modulo to implement the shift and decode operations respectively.
        temp = str((int(element) - 3) % 10)

        # tack on the decoded numbers to the string
        decoded_password += temp

    return decoded_password


def main():
    while True:
        menu()
        choice = input("Please enter an option: ")

        if choice == "1":
            code = input("Please enter your password to encode: ")
            x = encode(code)
            print("Your password has been encoded and stored!\n")

        elif choice == "2":
            print("the encoded password is", x, "and the original password is", code)

        elif choice == "3":
            exit()

        else:
            print("Wrong input. Please try again!")


if __name__ == '__main__':
    main()
