def prime_numbers(limit=100):
    primes = []
    for num in range(2, limit):
        is_prime = True
        for divisor in primes:
            if divisor * divisor > num:
                break
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(prime_numbers(100))

