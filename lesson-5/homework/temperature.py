def convert_cel_to_far():
    while True:
        user_input = input("Enter a temperature in degrees C: ")
        try:
            C = float(user_input)  
            F = C * 9/5 + 32
            print(f"{C} degrees C = {F} degrees F")
            break  
        except ValueError:
            print(f"Invalid input '{user_input}'. Please enter a valid float number.")

convert_cel_to_far()

def convert_far_to_cel():
    while True:
        user_input = input("Enter a temperature in degrees F: ")
        try:
            F = float(user_input)  
            C = (F - 32) * 5/9
            print(f"{F} degrees F = {C} degrees C")
            break  
        except ValueError:
            print(f"Invalid input '{user_input}'. Please enter a valid float number.")

convert_far_to_cel()
