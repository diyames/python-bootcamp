"""
# TODO: Ask the user for an integer input
number = int(input("Pick a number: "))

# TODO: Print the multiplication table for that number
"""
"""
Example:
number = 3

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
"""

number = int(input("Enter a number to multipy: "))

def multiplication_table(x):
    for minuend in range(1, 10 + 1):
        print(f" {minuend} * {x} = {minuend * x}")

multiplication_table(number)