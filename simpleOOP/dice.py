#! /usr/bin/env python3
__author__ = 'sihart'

''' A very simple example to start illustrating Class, Objects and Attributes'''
import random

class Dice():

    def __init__(self):
        self.sides = [1,2,3,4,5,6]

    #def __repr__(self):
      #  return('A dice object')

    def roll(self):
        print(self.sides[random.randint(0,5)])