#! /usr/bin/env python3
__author__ = 'sihart'

import sys

a = sys.argv[1]
len(sys.argv)

if len(sys.argv) > 2:
    print('\n Only one argument please\n')
    sys.exit()

if len(a)!= 1:
    print("\nOnly one character allowed as an argument\n")
    sys.exit()


if ord(a)< 127:
    print('\n\nThis character is within the ASCII range.  Unicode and ASCII codepoint are the same\n')
    print('In ASCII, Unicode and UTF-8  \''+a+'\'  is represented as ', hex(ord(a)), 'in hex notation\n')
    print('UTF-8 encoding for \''+a+'\' is represented as ', bin(int.from_bytes(a.encode('utf-8'), byteorder='big')),
          ' in binary\n')

else:

    print()
    print('Unicode Codepoint for \''+a+'\'  is represented as ', hex(ord(a)))
    print()
    print('UTF-8 encoding for \''+a+'\'  is represented as ', str(a.encode('utf-8'))[3:len(str(a.encode('utf-8')))-1], ' in hex')
    print()
    print('UTF-8 encoding for \''+a+'\'  is represented as ', bin(int.from_bytes(a.encode('utf-8'), byteorder='big')), ' in binary')
    print()