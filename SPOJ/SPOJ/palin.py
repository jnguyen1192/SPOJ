from sys import stdin, stdout


def analyse_palin(expression):
    res = ""
    length = expression.__len__()-1
    if length & 1:
    # Case 1 odd
    # Copier les memes chiffres jusqu a la moitie et ajouter +1 a celui du milieu
        for c in xrange(0, length/2):
            res += expression[c]
        res += str(int(expression[length/2])+1)
        for c in xrange(length/2-1, -1, -1):
            res += expression[c]
    else:
    # Case 2 even
    # Copier les memes chiffres jusqu a la moitie et ajouter +1 au dernier
        for c in xrange(0, length/2-1):
            res += expression[c]
        res += str(int(expression[length/2-1])+1)
        for c in reversed(res):
            res += c

    # string size <= 10^7
    # fun = 0
    # fun = mid string * 2
    # if fun < K
    #    +1 last mid char
    #    fun ++
    #    go to if
    # expression = fun
    res += "\n"
    return res


def palin():
    nb_line = int(stdin.readline())
    while nb_line != 0:
        expression = stdin.readline()
        stdout.write(analyse_palin(expression))
        nb_line -= 1
