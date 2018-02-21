from sys import stdin, stdout
import math


def clean_begin_zero(number):
    count = 0
    for i in number:
        if i == '0':
            count += 1
        else:
            break
    return number[count:]


def analyse_arith(expression):
    res = ''
    pos = expression.find('+')
    if pos != -1:
        res = add_or_sub_string_print(expression[0:pos], expression[pos+1:], '+')
    else:
        pos = expression.find('-')
        if pos != -1:
            res = add_or_sub_string_print(expression[0:pos], expression[pos + 1:], '-')
        else:
            pos = expression.find('*')
            # case mul_string_print(str1, str2)
    return res
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
    if str1 == str2:
        return '0'
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
def mul_string(str1, str2):
    if str2 == '1':
        return str1
    if str2 == '0':
        return '0'
    p1 = str1.__len__() - 1
    num2 = int(str2)
    l = []
    ret = 0
    while p1 > -1 or ret == 1:
        if p1 < 0:
            num1 = 0
        else:
            num1 = int(str1[p1])
        if ret > 0:
            mul = num1 * num2 + ret
            ret = 0
        else:
            mul = num1 * num2
        if mul > 9:
            ret = mul // 10 ** (int(math.log(mul, 10)) - 1 + 1)
            #https://stackoverflow.com/questions/41271299/how-can-i-get-the-first-two-digits-of-a-number
            mul %= 10
        l.append(str(mul))
        p1 -= 1
    if ret > 0:
        l.append(str(ret))
    return "".join(l)[::-1]


# add or sub string print
def add_or_sub_string_print(str1, str2, op):
    if op == '+':
        res = add_string(str1, str2)
    else:
        res = sub_string(str1, str2)
    lengthres = res.__len__()
    lengthstr1 = str1.__len__()
    lengthstr2 = str2.__len__()
    nbespacestr1 = 0
    nbespacestr2 = 0
    nbespaceres = 0
    if lengthres <= lengthstr2 and lengthstr1 <= lengthstr2:
        nbespacestr1 = lengthstr2 + 1 - lengthstr1
        tiret = '-' * (lengthstr2 + 1)
        nbespaceres = lengthstr2 + 1 - lengthres
    elif lengthres <= lengthstr1 and lengthstr2 <= lengthstr1:
        nbespacestr2 = lengthstr1 - lengthstr2 - 1
        tiret = '-' * lengthstr1
        nbespaceres = lengthstr1 - lengthres
    else:
        nbespacestr1 = lengthres - lengthstr1
        nbespacestr2 = lengthres - lengthstr2 - 1
        tiret = '-' * lengthres
    str1 = nbespacestr1 * ' ' + str1
    str2 = nbespacestr2 * ' ' + op + str2
    res = nbespaceres * ' ' + res
    return str1 + '\n' + str2 + '\n' + tiret + '\n' + res


# mul string print


def arith(nb_line):
    res = ""
    listres = []
    while nb_line != 0:
        expression = stdin.readline()
        listres.append(analyse_arith(expression[:-1]) + '\n' * 2)
        nb_line -= 1
    res = res.join(listres)
    stdout.write(res[:-2])
