from sys import stdin, stdout


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
