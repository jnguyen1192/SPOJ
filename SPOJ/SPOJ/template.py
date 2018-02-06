from sys import stdin, stdout


def analyse_template(expression):
    return expression


def template():
    nb_line = int(stdin.readline())
    while nb_line != 0:
        expression = stdin.readline()
        stdout.write(analyse_template(expression))
        nb_line -= 1
