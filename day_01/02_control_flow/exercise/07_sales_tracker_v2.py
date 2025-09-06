# TODO: Ask the user how many items will be calculated
input_count = int(input("Enter number: "))
total = 0


for number in range(1, input_count + 1):
    item_cost = int(input(f"Enter item {number} cost: "))
    item_count = int(input(f"Enter item {number} count: "))
    item_total = item_cost * item_count
    total += item_total
print(total)

"""
for items in range(1, input_count + 1):
    item_cost = int(input("Input Item Cost: "))
    item_count = int(input("Input Item Count: "))
    item_total = item_cost * item_count
    total += item_total
print(total)
"""

""""
# TODO: Use a for loop to ask for more than one cost and count
item_cost = None  # Let the user enter a number
item_count = None  # Let the user enter a number
item_total = item_cost + item_count

print(total)
"""

"""
for number in range(1, input_count + 1):
    item_cost = int(input(f"Enter item {number} cost: "))
    item_count = int(input(f"Enter item {number} count: "))
    item_total = item_cost * item_count
    total += item_total

print(total)
"""