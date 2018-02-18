#!/usr/bin/python
from sys import stdin, stdout
import re


def add1tostring(number):
    s = list(number)
    retained = 1
    nb_char = number.__len__()-1
    zero = 0
    while retained == 1 and nb_char >= 0:
        s[nb_char] = str(int(number[nb_char]) + 1)
        retained = 0
        if s[nb_char] == '10':
            s[nb_char] = '0'
            retained = 1
            nb_char -= 1
            zero += 1
    # Case +1 digit
    if zero == number.__len__():
        s = ['1'] + s
    return "".join(s)


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


def except_nine(number):
    res = ""
    listres = []
    for i in number:
        listres.append('9')
    res = res.join(listres)
    return number == res


def except_digit(number, digit):
    res = ""
    listres = []
    for i in number:
        listres.append(digit)
    res = res.join(listres)
    return number == res


def clean_begin_zero(number):
    count = 0
    for i in number:
        if i == '0':
            count += 1
        else:
            break
    return number[count:]


def clean_alpha_from_string(number):
    return re.sub('[^0-9]', '', number)


def find_next_palin(number):
    if except_digit(number, '0'):
        return '1'
    if except_digit(number, '9'):
        return add1tostring(add1tostring(number))
    length = number.__len__()
    sub = number[0:length/2]
    odd = ""
    end = number[length/2:length]
    if length & 1:
        odd = number[length/2]
        end = number[length / 2 + 1:length]
        if inf_str_int(sub, end):
            odd = str(int(odd) + 1)
            if odd == '10':
                odd = '0'
                sub = add1tostring(sub)
    else:
        if inf_str_int(sub, end):
            sub = add1tostring(sub)
    return sub + odd + sub[::-1]


def analyse_palin(expression):
    res = expression
    res = clean_alpha_from_string(res)
    res = clean_begin_zero(res)
    while True:
        pal = find_next_palin(res)
        res = add1tostring(res)
        if is_palin(pal) and pal != expression:
            break
    pal += "\n"
    return pal


def palin():
    nb_line = int(stdin.readline())
    res = ""
    listres = []
    while nb_line != 0:
        expression = stdin.readline()
        listres.append(analyse_palin(expression.replace(" ", "").replace("\n", "")))
        nb_line -= 1
    res = res.join(listres)
    stdout.write(res[:-1])


def main():
    palin()

if __name__ == "__main__":
    main()
