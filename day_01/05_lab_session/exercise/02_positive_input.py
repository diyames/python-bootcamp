# TODO: Ask the user for an input that should be a number
number = input("Enter number: ")

# TODO: Then try to convert this into an integer using the following:
number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case

# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry













def positive_input():
    while True:
        number = input("Enter number: ")

        try:
            number = int(number)

            if number < 0:
                raise ValueError("Number cannot be negative.")

            return number

        except ValueError:
            print("Please enter a positive number.")


positive_input()
print("Entered:", positive_input())
