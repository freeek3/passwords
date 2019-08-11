import random
import sys
import time

import pyperclip
import argparse


def __init__():
    parser = create_parser()
    args = parser.parse_args()

    time_start = time.time()
    if args.length < 2:
        length = 16
    elif args.length < 8:
        length = 8
    elif args.length > 64 and not args.length:
        length = 64
    else:
        length = args.length
    print("Generating Password with %s chars \n" % str(length))
    if args.sentence is None:
        password = random_password(length, args.char)
    else:
        password = sentence_password(length, args.sentence)

    time_stop = time.time()

    print("\nRemember " + password[0] + " and use " + "".join(password[1]))
    print("Took %s seconds to generate the password" % str(round(time_stop - time_start, 6)))
    if not args.clipboard or args.restore is not None:
        old = pyperclip.paste()
        pyperclip.copy("".join(password[1]))
        print("Passowrd coppied to clipboard")
        print("Your old clipboard: " + old)
        if args.restore is not None:
            time.sleep(int(args.restore))
            pyperclip.copy(old)
            print("old clipboard is restored")


def random_password(length=16, s=False):
    if length % 2 == 0:
        length -= 2
    else:
        length -= 1

    password = ""

    if not s:
        con = ['r', 't', 'z', 'u', 'i', 'o', 'p', 's', 'd',
               'f', 'g', 'h', 'j', 'k', 'l', 'v', 'b', 'n', 'm']
    else:
        con = ['q', 'w', 'r', 't', 'z', 'u', 'i', 'o', 'p', 's', 'd', 'f',
               'g', 'h', 'j', 'k', 'l', 'y', 'x', 'c', 'v', 'b', 'n', 'm']

    voc = ['a', 'e', 'i', 'o', 'u']

    l33t = [['a', '4'], ['s', '5', '$', '§'], ['e', '3', '€'], ['i', '!'], ['g', '9'],
            ['b', '8'], ['o', '0'], ['t', '7'], ['l', '1'], ['p', '%']]  # ['r', '|2']

    num = [['1', '!'], ['2', '"'], ['3', '§'], ['4', '$'], ['5', '%'],
           ['6', '&'], ['7', '/'], ['8', '#'], ['9', '?'], ['0', '=']]

    password += con[random.randrange(len(con))].swapcase()
    for i in range(1, int(length / 2)):
        password += con[random.randrange(len(con))]
        password += voc[random.randrange(len(voc))]
        print(password)

    if length % 2 == 0:
        length += 2
        password += str(random.randrange(10, 100))
    else:
        length += 1
        password += str(random.randrange(1, 10))

    p = list(password)

    for i in range(1, len(p)):
        for j in range(0, len(l33t)):
            if p[i] == l33t[j][0]:
                if random.randrange(3) > 0:  # l33t replace change
                    if len(l33t[j]) > 2:
                        p[i] = l33t[j][random.randrange(len(l33t[j]))]

                    else:
                        p[i] = l33t[j][1]
                    print("".join(p))
                else:  # swapcase chance
                    if random.randrange(5) < 2:
                        p[i].swapcase()
                    print("".join(p))

    for i in range(0, len(num)):  # special char chance
        if length % 2 == 0:
            if p[length - 3] == num[i][0]:
                if random.randrange(4) > 0:
                    p[length - 3] = num[i][1]
                    print("".join(p))
        else:
            if p[length - 2] == num[i][0]:
                if random.randrange(3) > 0:
                    p[length - 2] = num[i][1]
                    print("".join(p))

    return [password, p]


def sentence_password(length=16, file=None):
    return ["not implemented", "not implemented"]


def create_parser():
    p = argparse.ArgumentParser(description='Create Rememberable passwords')
    p.add_argument('length', metavar='L', type=int, default=16, nargs='?',
                   help='Length of the password')
    p.add_argument('-l', '--length', help='disable max length', action='store_true')
    p.add_argument('-c', '--char', help='use special chars if possible', action='store_true')
    p.add_argument('-s', '--sentence', help='use a sentence generator, with provided dictonary file',
                   type=argparse.FileType('r', encoding='UTF-8'), metavar='FILE')
    p.add_argument('-b', '--clipboard', help='don\'t copy password to clipboard', action='store_true')
    p.add_argument('-r', '--restore', help='restore old clipboard after some time', metavar='SECONDS', type=int)

    return p


__init__()
