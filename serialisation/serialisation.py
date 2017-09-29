#! /usr/bin/env python3
__author__ = 'sihart'

'''some code to demonstrate serialisation with UTF-8'''
a = 'a'

print('In ASCII, Unicode and UTF-8  \'a\' is represented as ', ord(a), 'in decimal notation')
print()
print('In ASCII, Unicode and UTF-8 \'a\' is represented as ', hex(ord(a)), 'in hex notation')
print()
print('In ASCII, Unicode and UTF-8 \'a\' represented as ' ,bin(ord(a)), 'binary notation')
print()
print()
print('Unicode Codepoint for \'😀\' is represented as ', hex(ord('😀')))
print()
print('UTF-8 encoding for \'😀\' is represented as ', '😀'.encode('utf-8') )
print()
print('UTF-8 encoding for \'😀\' is represented as ', bin(int.from_bytes('😀'.encode('utf-8'), byteorder='big')), ' in binary')
print()
print('Unicode Codepoint for \'b\' is represented as ', hex(ord('b')))
print()
print('UTF-8 encoding for \'b\' is represented as ', 'b'.encode('utf-8') )
print()
print('UTF-8 encoding for \'b\' is represented as ', bin(int.from_bytes('b'.encode('utf-8'), byteorder='big')), ' in binary')