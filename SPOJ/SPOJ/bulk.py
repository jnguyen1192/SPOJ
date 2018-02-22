from sys import stdin, stdout


def analyse_bulk(expression):
    return expression


def bulk():
    nb_line = int(stdin.readline())
    res = ""
    listres = []
    while nb_line != 0:
        expression = stdin.readline()
        listres.append(analyse_bulk(expression[:-1] + '\n' * 1))
        nb_line -= 1
    res = res.join(listres)
    stdout.write(res[:-1])
