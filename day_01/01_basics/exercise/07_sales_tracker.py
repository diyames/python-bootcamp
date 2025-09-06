# Ask the cost and pax or count for three separate items
from itertools import count

item_cost_1 = int(input("Enter Item Cost 1: "))
item_count_1 = int(input("Enter Item Count 1: "))

item_cost_2 = int(input("Enter Item Cost 2: "))
item_count_2 = int(input("Enter Item Count 2: "))

item_cost_3 = int(input("Enter Item Cost 3: "))
item_count_3 = int(input("Enter Item Count 3: "))
# Calculate the total

total = (item_cost_1 * item_count_1) + (item_cost_2 * item_count_2) + (item_cost_3 * item_count_3)
print(total)