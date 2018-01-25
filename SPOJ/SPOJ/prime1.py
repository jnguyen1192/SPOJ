from math import *


def find_prime_between(start, end):
    j = int(start)
    res = ""
    while j < int(end) + 1:
        if is_prime(j):
            res += str(j) + "\n"
        j += 1
    return res


def prime1():
    nbline = input()
    for i in range(0, nbline):
        string = raw_input()
        twin = string.split()
        print find_prime_between(twin[0], twin[1])


def m_range(start, stop, step):
    while start < stop:
        yield start
        start += step
# https://stackoverflow.com/questions/3220907/efficient-algorithm-to-get-primes-between-two-large-numbers


def get_low_primes(num):
    j = 1
    res = []
    while j < int(num) + 1:
        if is_prime(j):
            res.append(j)
        j += 1
    return res

def is_prime(num):
    # Constraints
    if num == 2 or num == 5:
        return True
    if num < 2 or num % 10 == 5 or num % 2 == 0:
        return False
    # Small prime between 1 and 29100000 because time is less than 3.1 second
    if num < 29100000:
        return all(num % i for i in m_range(3, int(sqrt(num)) + 1, 2))
    # Mid prime between 60100000 and 529000000
    if num < 529000000:
        lowPrimes = midPrimes
    # Big prime between 529000000 and 1000000000
    else:
        lowPrimes = bigPrimes

    if num in lowPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if num % prime == 0:
            return False
    # It s a prime number
    return True
    #return all(num % i for i in m_range(begin, int(sqrt(num)) + 1, 2))


midPrimes = get_low_primes(23101)
bigPrimes = get_low_primes(32101)