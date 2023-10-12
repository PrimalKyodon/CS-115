##############################################
#   Name: Aaren Patel
#   CS 115 Lab 2
#   I pledge my honor that I have abided by the Stevens Honor System
#
##############################################

def dot(L, K):
    """Returns the dot product of the two lists L and K"""
    if L == []:
        return 0
    return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    """Returns the string S as a list with one letter in each index"""
    if S =="":
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    """Returns the index at which e is in the list L; Returns len if no e exists in L"""
    if L == [] or L=="" or L[0] == e:
        return 0
    return 1 + ind(e, L[1:])

def removeAll(e, L):
    """Returns the list L without any values e"""
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

def even(x):
    return x%2 == 0

def myFilter(f, L):
    """Filters out the values that satisfy the function f from the list L"""
    if L == []:
        return []
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    return [] + myFilter(f, L[1:])

def deepReverse(L):
    """Reverses the values in L as well as any embedded lists"""
    if L == []:
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    return deepReverse(L[1:]) + [L[0]]
