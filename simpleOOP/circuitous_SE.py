#! /usr/bin/env python3
__author__ = 'sihart'

from random import random

from simpleOOP.SE_OOP_Circle import Circle

n = 5
#seed(40)

#Generator example.  List comprehension with () creates generator

circles = (Circle(random()) for i in range(n))
areas = (c.area() for c in circles)
summary = sum(areas) / n
print("The average radius for generator circles is ", summary)

#List comprehension but using a [], which creates a list that can be iterated over

circles2 = [Circle(random()) for i in range(n)]
areas = [c.area() for c in circles2]
summary2 = sum(areas) / n
print("The average radius for iterator circles is ", summary2)
