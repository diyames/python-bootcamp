# Ask the user input for a color
color_input = input("Please enter a color: ")

# TODO: Print the following depending on the color input
# "green"   -> print "Go"
if color_input == "green":
    print("Go")
# "yellow"  -> print "Wait..."
elif color_input == "yellow":
    print("Wait...")
# "red"     -> print "Stop"
elif color_input == "red":
    print("Stop")
else:
    print("Malfunction")

"""
# TODO: Print the following depending on the color input
match color_input:
    case "green" | "Green":
        print("Go")
    case "yellow" | "Yellow":
        print("Wait...")
    case "red" | "Red":
        print("Stop")
    case _:
        print("Malfunction")
"""