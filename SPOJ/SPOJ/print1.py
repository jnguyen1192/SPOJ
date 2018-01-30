from math import *
import time


def print1():
    from sys import stdin, stdout
    nb_line = stdin.readline()
    t0 = time.clock()
    res = ""
    for i in range(0, int(nb_line)):
        string = stdin.readline()
        twin = string.split()
        res += primesRange(int(twin[0]), int(twin[1]), int(twin[1]) - int(twin[0]))
    # optimisation pour la fusion de boucle
    stdout.write(res)
    t = time.clock() - t0
    print str(t) + " seconds"


def primes(n):
    ps, sieve = [], [True] * n
    for p in range(2, n):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n, p):
                sieve[i] = False
    return ps


arrayMidPrimes = primes(23101)
arrayBigPrimes = primes(32101)
arrayLimitPrime = primes(46441)


def primesRange(lo, hi, delta):
    # Dirty 1
    hi += 1
    def qInit(p):
        return ((lo + p + 1) / -2) % p

    def qReset(p, q):
        return (q - delta) % p
    res = ""
    output, sieve = [], [True] * delta
    if hi < 529000000:
        ps = arrayMidPrimes[1:]
        # Big prime between 529000000 and 1000000000
    elif hi < 1000000000:
        ps = arrayBigPrimes[1:]
        # Limit prime between 1000000000 and 2147483647
    else:
        ps = arrayLimitPrime[1:]
    # Dirty 2
    if 9 < hi < 16:
        ps = [3]
    qs = map(qInit, ps)
    # Dirty 3
    if lo == 2:
        res += str(2) + "\n"
    # Dirty 4
    if lo == 3 and hi < 15:
        res += str(3) + "\n"
    # Dirty 5
    if lo < int(sqrt(hi)):
        for i in ps:
            res += str(i) + "\n"
    while lo < hi:
        sieve[0::1] = [True] * ((delta - 0 - 1) // 1 + 1)
        for p, q in zip(ps, qs):
            sieve[q::p] = [False] * ((delta - q - 1) // p + 1)
        qs = map(qReset, ps, qs)
        for i, t in zip(range(0, delta), range(lo + 1, hi, 2)):
            if sieve[i]:
                if t <= hi - 1:
                    if t % 2 == 0:
                        res += str(t + 1) + "\n"
                        #output.append(t + 1)
                    else:
                        res += str(t) + "\n"
                        #output.append(t)
        lo += (2 * delta)
    return res
#https://ideone.com/iHYr1f
#https://codereview.stackexchange.com/questions/42420/sieve-of-eratosthenes-python
