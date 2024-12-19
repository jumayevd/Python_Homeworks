def factors(number):
    for i in range(1, number+1):
        if number % i == 0:
            print(f"{i} is a factor of {number}")

try:
    number = int(input("Enter a positive integer: "))
    if number <= 0:
        raise ValueError("The number must be positive.")
    factors(number)
except ValueError as e:
    print(f"Invalid input: {e}")




