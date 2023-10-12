###############################################
#   Name: Aaren Patel
#   Date: 9/28/2022
#   CS 115 HW 2
#   I pledge my honor that I have abided by the Stevens Honor System.
#
##############################################

import sys
from functools import reduce

sys.setrecursionlimit(10000)
# Leave the following lists in place.
scrabbleScores = [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2], ['h', 4],
                   ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],['o', 1], ['p', 3], ['q', 10],
                   ['r', 1], ['s', 1], ['t', 1], ['u', 1],['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]
Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


def letterScore(letter, scoreList):
    if scoreList == []:
        return 0
    elif letter == scoreList[0][0]:
        return scoreList[0][1]
    return letterScore(letter, scoreList[1:])
    
def wordScore(S, scoreList):
    if S == "":
        return 0
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)




def listWords(Rack):
    L = []


#def scoreList(Rack):
    



    
def bestWord(Rack):
    return reduce(lambda x, y: x if x[1] > y[1] else y, scoreList(Rack))
