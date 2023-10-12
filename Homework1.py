#########################################################
#   Name: Aaren Patel
#   Pledge: I pledge my honor that I have abided by the Stevens Honor System
#   Class: CS 115
#   Assignment: Homework 1
#
#########################################################


from functools import reduce

def mult(x, y):
    """returns the value of x times y"""
    return x*y

def factorial(x):
    """returns the value of x!"""
    return reduce(mult, range(1, x+1))

def add(x, y):
    """returns the value of x plus y"""
    return x+y

def mean(L):
    """returns the mean of the values within the list L"""
    if L == []:
        return 0
    return reduce(add, L)/len(L)
