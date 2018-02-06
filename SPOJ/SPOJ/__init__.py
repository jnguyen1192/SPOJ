#!/usr/bin/python
from sys import stdin, stdout


def add1tostring(number):
    res = ""
    retained = 1
    nb_char = len(number) / 2
    if len(number) & 1:
        nb_char += 1
    while nb_char > -1:
        if int(number[nb_char]) == 9:
            res += str(0)
        elif retained == 1:
            res += str(int(number[nb_char]) + 1)
            retained -= 1
        else:
            res += str(int(number[nb_char]))
        nb_char -= 1
    return res[::-1]


def analyse_palin(expression):
    res = ""
    length = len(expression)-1
    if length & 1:
        for c in xrange(0, length/2 + 1):
            res += expression[c]
        if int(expression[length / 2 - 1]) < int(expression[length / 2]) or int(expression[length / 2]) == 0:
            res = add1tostring(res)
        for c in reversed(res[:-1]):
            res += c
    else:
        for c in xrange(0, length/2):
            res += expression[c]
        if int(expression[length/2-1]) < int(expression[length/2]):
            res = add1tostring(res)
        for c in reversed(res):
            res += c
    res += "\n"
    return res


def palin():
    nb_line = int(stdin.readline())
    res = ""
    while nb_line != 0:
        expression = stdin.readline()
        res += analyse_palin(expression)
        nb_line -= 1
    stdout.write(res)


def main():
    palin()

if __name__ == "__main__":
    main()
