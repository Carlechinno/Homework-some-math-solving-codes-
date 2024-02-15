

def is_prime(n: int):
    if n <= 1:  # 1 is not a prime number
        return False
    if n <= 3: # 2 and 3 are prime numbers and 1 is not
        return True


    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if (n % i == 0 or
                n % (i + 2) == 0):
            return False
        i = i + 6

    return True


def factor_sum(x:int):
    sum = 0
    for i in range(1, x-1):
        if x % i == 0:
            if is_prime(i):
                sum += i

    return sum
