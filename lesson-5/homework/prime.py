def is_prime(n):
    if n <= 1:  
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True  

try:
    number = int(input("Enter a positive integer: "))
    if number < 0:
        print("The number must be positive!")
    else:
        print(is_prime(number))
except ValueError:
    print("Enter a valid positive integer!")
