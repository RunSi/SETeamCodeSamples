#! /usr/bin/env python3
__author__ = 'sihart'

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='append', dest="vlans", default=[], help='add vlan in the format vlan-200')


results = parser.parse_args()

if not results.vlans:
    print('Please enter vlans with -v operator')
    sys.exit()

print("\nThese are the vlans you entered")
print(results.vlans)

newvlans = []

newvlans = [r'"' + x + r'"' for x in results.vlans]

print('\nThis is the first vlan in the list')
print(newvlans[0])