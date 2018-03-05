#!/usr/bin/python
from sys import stdin, stdout


def analyse_fctrl(expression):
    # @source http://www.purplemath.com/modules/factzero.htm
    if expression < 4:
        return "0"
    calc = 2
    exp = 1
    nums = []
    while calc >= 1:
        calc = expression / pow(5, exp)
        if calc >= 1:
            nums.append(calc)
        exp += 1
    return str(sum(nums))


def fctrl(nb_line):
    res = ""
    listres = []
    while nb_line != 0:
        expression = stdin.readline()
        listres.append(analyse_fctrl(int(expression.replace("\n", ""))) + '\n')
        nb_line -= 1
    res = res.join(listres)
    stdout.write(res[:-1])



def main():
    fctrl(int(stdin.readline()))

if __name__ == "__main__":
    main()
