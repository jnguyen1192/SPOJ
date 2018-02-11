import random

numberdigits = 1000000


def generate():
    t = 10
    print t
    while t > 0:
        res = ""
        knumberdigit = random.randint(2, numberdigits)
        for i in xrange(0, knumberdigit):
            kdigit = random.randint(1, 9)
            res += str(kdigit)
        print res
        t -= 1
    print ""
