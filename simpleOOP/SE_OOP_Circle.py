#! /usr/bin/env python3
__author__ = 'sihart'

# Intro to Object Oriented Programming
# Introduces classes with a Circle application

class Circle():

    '''Creates some fantastic circle maths - a simple Simon Hart Class'''

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        fmt = '{}(Radius={!r})'
        return fmt.format(type(self).__name__, self.radius)


    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 3.14 * self.radius * 2