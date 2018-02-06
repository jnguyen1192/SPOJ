from sys import stdin, stdout


def analyse_palin(expression):
    # Case 1 odd
    # Copier les memes chiffres jusqu a la moitie et ajouter +1 a celui du milieu

    # Case 2 even
    # Copier les memes chiffres jusqu a la moitie et ajouter +1 au dernier

    # string size <= 10^7
    # fun = 0
    # fun = mid string * 2
    # if fun < K
    #    +1 last mid char
    #    fun ++
    #    go to if
    # expression = fun
    return expression


def palin():
    nb_line = int(stdin.readline())
    while nb_line != 0:
        expression = stdin.readline()
        stdout.write(analyse_palin(expression))
        nb_line -= 1
