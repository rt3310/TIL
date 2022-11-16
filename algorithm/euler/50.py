primes = []

total = 0
def is_prime(n):
    global primes
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in primes:
        if n % i == 0:
            return False
    return True

for i in range(1, 1000001):
    if is_prime(i):
        primes.append(i)
        print(i)

print(primes)