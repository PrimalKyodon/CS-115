######################################################
#   Name: Aaren Patel
#   Pledge: I pledge my honor that I have abided by the Stevens Honor System
#   CS115 - Lab 1
#
######################################################

from math import factorial
from functools import reduce


def inverse(x):
    """returns the reciprocal of the input value"""
    return 1/x

def add(x, y):
     """returns the sum of x and y"""
     return x+y

def e(n):
    """returns the taylor polynomial sum for e with n terms """
    return reduce(add, map(inverse, map(factorial, range(n+1))))
