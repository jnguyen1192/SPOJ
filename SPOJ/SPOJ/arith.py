from sys import stdin, stdout


def analyse_arith(expression):
    return " 12345\n+67890\n------\n 80235"
# keep number 1
# keep operator
# keep number 2

# add string
def add_string(str1, str2):
    p1 = str1.__len__() - 1
    p2 = str2.__len__() - 1
    l = []
    ret = 0
    while (p1 > -1 and p2 > -1) or ret == 1:
        if ret == 1:
            ret = 0
            if p1 < 0:
                num1 = 0
            else:
                num1 = int(str1[p1])
            if p2 < 0:
                num2 = 0
            else:
                num2 = int(str2[p2])
            add = num1 + num2 + 1
        else:
            num1 = int(str1[p1])
            num2 = int(str2[p2])
            add = num1 + num2
        if add > 9:
            add %= 10
            ret = 1
        l.append(str(add))
        p1 -= 1
        p2 -= 1
    return "".join(l)[::-1]

# sub string
# mul string

def arith():
    nb_line = int(stdin.readline())
    while nb_line != 0:
        expression = stdin.readline()
        stdout.write(analyse_arith(expression))
        nb_line -= 1