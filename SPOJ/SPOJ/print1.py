from math import *

import math
import time
#46331 46341


def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n + 1, i)]
        p = [x for x in range(2, n + 1) if x not in no_p]
        return p


def sieveofatkin(start, limit):
    if start < 5:
        P = [2, 3]
    else:
        P = []
    sieve = [False]*(limit+1)
    for x in range(1, int(math.sqrt(limit))+1):
        for y in range(1, int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5 + start, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit+1, x**2):
                sieve[y] = False
    for p in range(5 + start, limit):
        if sieve[p]:
            P.append(p)
    return P


def find_prime_between(start, end):
    j = int(start)
    #Reduc time test all odd
    res = ""
    if j == 2:
        j += 1
        res += str(2) + "\n"
    if j % 2 == 0:
        j += 1
    while j < int(end) + 1:
        if is_prime(j):
            res += str(j) + "\n"
        j += 2
    return res[:-1]


def print1():
    from sys import stdin, stdout
    nb_line = stdin.readline()
    for i in range(0, int(nb_line)):
        string = stdin.readline()
        twin = string.split()
        stdout.write(find_prime_between(int(twin[0]), (twin[1])))


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


def are_prime(start, end):
    list = [True] * (end - start)
    primesrootlastnumber = get_low_primes(sqrt(end))
    for i in primesrootlastnumber:
        for j in range(0, (end - start)):
            if not list[j]:
                continue
            if (j + start) % i == 0:
                list[j] = False
    primesfind = []
    for i in primesrootlastnumber:
        if i >= start:
            primesfind.append(i)
    for i in range(0, (end - start)):
        if list[i]:
            primesfind.append(i + start)
    return primesfind


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
    elif num < 529000000:
        lowPrimes = midPrimes
    # Big prime between 529000000 and 1000000000
    elif num < 1000000000:
        lowPrimes = bigPrimes
    # Limit prime between 1000000000 and 2147483647
    else:
        lowPrimes = limitPrimes
    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if num % prime == 0:
            return False
    # It s a prime number
    return True

midPrimes = get_low_primes(23101)
bigPrimes = get_low_primes(32101)
limitPrimes = get_low_primes(46441)
#sqrt(2147483647) + 101


def primes(n):
    ps, sieve = [], [True] * (n)
    for p in range(2, n):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    return ps


def primesRange(lo, hi, delta):
    hi += 1
    def qInit(p):
        return ((lo + p + 1) / -2) % p

    def qReset(p, q):
        return (q - delta) % p
    res = ""
    output, sieve = [], [True] * delta
    ps = primes(int(sqrt(hi)))[1:]
    if 9 < hi < 16:
        ps = [3]
    qs = map(qInit, ps)
    # Dirty 1
    if lo == 2:
        output.append(2)
    # Dirty 2
    if lo < int(sqrt(hi)):
        for i in ps:
            output.append(i)
    while lo < hi:
        for i in range(0, delta):
            sieve[i] = True
        for p, q in zip(ps, qs):
            for i in range(q, delta, p):
                sieve[i] = False
        qs = map(qReset, ps, qs)
        for i, t in zip(range(0, delta), range(lo + 1, hi, 2)):
            if sieve[i]:
                if t % 2 == 0:
                    output.append(t + 1)
                else:
                    output.append(t)
        lo += (2 * delta)
    for i in output:
        res += str(i) + "\n"
    return res[:-1]
#https://ideone.com/iHYr1f
