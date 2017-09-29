#! /usr/bin/env python3
__author__ = 'sihart'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', action='append', dest="vlans", default=[], help='add vlan in the format \"vlan-200\"')

results = parser.parse_args()

print(results.vlans)

newvlans = []

newvlans = [r'"' + x + r'"' for x in results.vlans]

print(newvlans[0])