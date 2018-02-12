#!/usr/bin/python
from sys import stdin, stdout


def add1tostring(number):
    res = ""
    retained = 1
    nb_char = number.__len__()-1
    zero = 0
    while nb_char > -1:
        if int(number[nb_char]) == 9 and retained == 1:
            res += str(0)
            zero += 1
        elif retained == 1:
            res += str(int(number[nb_char]) + 1)
            retained -= 1
        else:
            res += str(int(number[nb_char]))
        nb_char -= 1
    # Case +1 digit
    if zero == number.__len__():
        res = res + "1"
    #Modif only car we want
    return res[::-1]


def is_palin(number):
    length = number.__len__()
    for i in xrange(0, length/2):
        if number[i] != number[length-1-i]:
            return False
    return True


def inf_str_int(str1, str2):
    length = str1.__len__()
    for i in xrange(0, length):
        if int(str1[length - 1 - i]) < int(str2[i]):
            return True
        if int(str1[length-1-i]) > int(str2[i]):
            return False

    return True


def find_next_palin(number):
    length = number.__len__()
    sub = number[0:length/2]
    odd = ""
    rev = sub[::-1]
    end = number[length/2:length]
    if length & 1:
        odd = number[length/2]
        end = number[length / 2 + 1:length]
        if inf_str_int(sub, end):
            odd = str(int(odd) + 1)
        else:
            print sub
            print end
    else:
        if inf_str_int(sub, end):
            sub = add1tostring(sub)
            rev = sub[::-1]
    return sub + odd + rev


def analyse_palin(expression):
    res = add1tostring(expression[:-1])
    pal = "112"
    while True:
        if is_palin(pal) and res.find("0") == -1 and pal != expression[:-1]:
            break
        pal = find_next_palin(res)
        res = add1tostring(res)
    pal += "\n"
    return pal


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
