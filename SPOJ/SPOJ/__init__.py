#!/usr/bin/python
from sys import stdin, stdout


def luae():
    while True:
        number = stdin.readline()
        if int(number) == 42:
            break
        stdout.write(number)


def main():
    luae()

if __name__ == "__main__":
    main()
