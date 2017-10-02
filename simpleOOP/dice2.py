#! /usr/bin/env python3
__author__ = 'sihart'

import random

class Dice():

    '''A simple dice object to demonstrate OOP.  Call using Dice(), optionally enter number of sides
    otherwise defaults to 6'''

    def __init__(self, sides=6):
        self.sides = sides

    def __repr__(self):
        return('A dice object with ' + str(self.sides) + ' sides')

    def roll(self):
        print(random.randint(1,self.sides))