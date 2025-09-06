def add(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total + total_item_cost
    """TODO: Add item cost (cost, count) from total and return"""


def sub(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total - total_item_cost
    """TODO: Remove item cost (cost, count) from total and return"""


def show(total):
    """TODO: Print total"""


def main():
    total = 0
    running = True
    while running:
        command = input("Provide command: ")
        if command == "add":
            total = add(total)
        elif command == "sub":
            total = sub(total)
        elif command == "show":
            print(total)
        elif command == "exit":
            running = False


main()
