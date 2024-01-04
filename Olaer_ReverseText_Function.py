def check_input(prompt):  # Check the input for 'yes' or 'no'
    while True:
        user_input = input(prompt).lower()
        if user_input in {'yes', 'no'}:
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.\n")


def input_again():  # Prompt user to choose to input another or no
    while True:
        another_input = check_input("Do you want to input another integer? (yes/no): ")
        if another_input == 'yes':
            print("")
            main()
        else:
            print("\n- - Exiting - -")
            exit()


def main():  # Main program flow
    while True:
        text_input = input("Enter a string: ")

        if not any(char.isdigit() for char in text_input):
            text_output = text_input[::-1]  # Slices string from end to start
            print("Output:", text_output, "\n")
            input_again()
        else:
            print("Error Reported! Enter text only.\n")


if __name__ == '__main__':
    main()
