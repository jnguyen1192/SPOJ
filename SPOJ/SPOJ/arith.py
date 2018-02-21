from sys import stdin, stdout


def clean_begin_zero(number):
    count = 0
    for i in number:
        if i == '0':
            count += 1
        else:
            break
    return number[count:]


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
    while (p1 > -1 or p2 > -1) or ret == 1:
        if p1 < 0:
            num1 = 0
        else:
            num1 = int(str1[p1])
        if p2 < 0:
            num2 = 0
        else:
            num2 = int(str2[p2])
        if ret == 1:
            ret = 0
            add = num1 + num2 + 1
        else:
            add = num1 + num2
        if add > 9:
            add %= 10
            ret = 1
        l.append(str(add))
        p1 -= 1
        p2 -= 1
    return "".join(l)[::-1]


# sub string
def sub_string(str1, str2):
    p1 = str1.__len__() - 1
    p2 = str2.__len__() - 1
    l = []
    ret = 0
    while (p1 > -1 or p2 > -1) or ret == 1:
        if p1 < 0:
            num1 = 0
        else:
            num1 = int(str1[p1])
        if p2 < 0:
            num2 = 0
        else:
            num2 = int(str2[p2])
        if ret == 1:
            ret = 0
            sub = num1 - num2 - 1
        else:
            sub = num1 - num2
        if sub < 0:
            sub = 10 + sub
            ret = 1
        l.append(str(sub))
        p1 -= 1
        p2 -= 1
    res = clean_begin_zero("".join(l)[::-1])
    if res == '':
        res = '0'
    return res
# mul string

def arith():
    nb_line = int(stdin.readline())
    while nb_line != 0:
        expression = stdin.readline()
        stdout.write(analyse_arith(expression))
        nb_line -= 1
