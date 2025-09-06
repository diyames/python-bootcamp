items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = ("spam")

for item in items:
    item_to_find = ("spam")
    if item == input("What item are you looking for?: "):
        print("Item Found:", item)
    if item != input("What item are you looking for?: "):
        print("Item not Found:")
    break

"""
for item in items:
    if item == item_to_find:
        print("Item found:", item_to_find)
        break
"""