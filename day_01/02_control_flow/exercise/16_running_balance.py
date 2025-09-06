total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        total += int(input("Enter number: "))
        print("Total:", total)
    if command == "sub":
        total -= int(input("Enter number: "))
        print("Total:", total)
    elif command == "exit":
        running = False


