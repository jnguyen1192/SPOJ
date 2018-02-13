import random

numberdigits = 1000000


def generate():
    file = open("palin.txt", "w")
    t = 10
    file.write(str(t) + "\n")
    while t > 0:
        res = ""
        knumberdigit = random.randint(2, numberdigits)
        for i in xrange(0, knumberdigit):
            kdigit = random.randint(1, 9)
            res += str(kdigit)
        file.write(res + "\n")
        print res
        t -= 1
    file.write("\n")
    file.close()
