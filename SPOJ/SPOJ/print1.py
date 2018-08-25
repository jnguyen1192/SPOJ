import time
from sys import stdin, stdout
import numpy
import math


def print1():
    nb_line = stdin.readline()
    res = ""
    listres = []
    t0 = time.clock()
    for i in xrange(0, int(nb_line)):
        string = stdin.readline()
        twin = string.split()
        listres.append(primesRange(int(twin[0]), int(twin[1]), int(twin[1]) - int(twin[0])))
    res = res.join(listres)
    # optimisation pour la fusion de boucle
    stdout.write(res)
    t = time.clock() - t0
    print str(t) + " seconds"

# TO DO
# Utiliser le meme tableau de nombre premier genere

'''
def primes(n):
    # Find all primes n > prime > 2 using the Sieve of Eratosthenes
    # For efficiency, track only odd numbers (evens are nonprime)

    sieve = numpy.ones(n / 2, dtype=numpy.bool)
    limit = int(math.sqrt(n)) + 1

    for i in range(3, limit, 2):
        if sieve[i / 2]:
            sieve[i * i / 2:: i] = False

    prime_indexes = numpy.nonzero(sieve)[0][1::]
    prms = 2 * prime_indexes.astype(numpy.int32) + 1
    return prms
'''

def primes(n):
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n

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
    listres = []
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
        listres.append(str(2) + "\n")
    # Dirty 4
    if lo == 3 and hi < 15:
        listres.append(str(3) + "\n")
    # Dirty 5
    if lo < int(hi ** .5):
        for i in ps:
            if i < hi:
                listres.append(str(i) + "\n")
    while lo < hi:
        # Prepare un tableau de 0 a la fin a true
        sieve[0::1] = [True] * ((delta - 0 - 1) // 1 + 1)
        # Lorsqu il y a multiple mettre faux
        for p, q in zip(ps, qs):
            sieve[q::p] = [False] * ((delta - q - 1) // p + 1)
        qs = map(qReset, ps, qs)
        # Afficher true
        for i, t in zip(xrange(0, delta), xrange(lo + 1, hi, 2)):
            if sieve[i]:
                if t <= hi - 1:
                    if t % 2 == 0:
                        listres.append(str(t + 1) + "\n")
                        #output.append(t + 1)
                    else:
                        listres.append(str(t) + "\n")
                        #output.append(t)
        lo += (2 * delta)
    res = res.join(listres)
    return res
#https://stackoverflow.com/questions/10249378/segmented-sieve-of-eratosthenes
#https://ideone.com/iHYr1f
#https://codereview.stackexchange.com/questions/42420/sieve-of-eratosthenes-python

