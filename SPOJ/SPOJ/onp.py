from sys import stdin, stdout


def is_pile(c):
    return c == '('


def is_depile(c):
    return c == ')'


def is_next_char(c):
    return c.isalpha()


def analyse_onp(expr):
    listres = []
    bracket = 0
    stack = []
    for c in expr:
        if is_pile(c):
            bracket += 1
        elif is_depile(c):
            bracket -= 1
            listres.append(stack[0])
            stack.pop(0)
        elif is_next_char(c):
            listres.append(c)
        else:
            stack.insert(0, c)
    listres.append("\n")
    if bracket != 0:
        return "Error\n"
    return "".join(listres)


def onp():
    nb_line = int(stdin.readline())
    while nb_line != 0:
        expression = stdin.readline()
        stdout.write(analyse_onp(expression))
        nb_line -= 1
