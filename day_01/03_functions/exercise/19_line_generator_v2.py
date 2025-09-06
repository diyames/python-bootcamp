"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number

	# TODO: Use the function once
"""
"""
def greeting(name):
    print(f"Hello, {name}! Nice to meet you!")

greeting("Bob")
"""
def line_generator(number):
    for line in range(number):
        print("Line {}".format(line+1))

line_generator(int(input("How many lines you want to generate: ")))

