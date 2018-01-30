import random

u = 2147483647
l = 2


def generate():
    t = 150
    print t
    while t > 0:
        int1 = random.randint(2, u-1)
        int2 = random.randint(int1, int1 + 1000000)
        while int2 > u:
            int2 = random.randint(int1, int1 + 1000000)
        print str(int1) + " " + str(int2)
        t -= 1
    print ""
