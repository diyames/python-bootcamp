minimum_height = 138

height = int(input("Enter User Height: "))
user_height = height   # User height (in cm)

# TODO: Notify user if they can enter the ride
can_enter_ride = minimum_height <= user_height
print("Can enter the ride:", can_enter_ride)
