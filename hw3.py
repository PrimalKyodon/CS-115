
#################################################
#       Name: Aaren Patel
#       Date: 10/6/22
#       I pledge my honor that I have abided by the Stevens Honor System.
#       CS115 Homework 3
#
#################################################

def giveChange(amount, coins):
        """Outputs the minimum amount of coins used to create amount and the coins used to make the total"""
        if amount == 0:
                return [0, []]
        if coins == []:
                return [float("inf"), []]
        if coins[0]>amount:
                return giveChange(amount, coins[1:])
        use = giveChange(amount-coins[0], coins)
        lose = giveChange(amount, coins[1:])
        use[0]+= 1
        use[1]+=[coins[0]]
        if use[0]>lose[0]:
                return lose
        return use
	

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo', 'spam', 'spammy', 'zzyzva']

def letterScore(letter, scorelist):
        """Outputs the scrabble score of a given letter"""
        if scorelist == []:
                return
        elif scorelist[0][0] == letter:
                return scorelist[0][1]
        else:
                return letterScore(letter, scorelist[1:])

def wordScore(word, scorelist):
        '''Outputs the scrabble score of a given word'''
        if len(word) == 1:
                return letterScore(word[0], scorelist)
        else:
                return letterScore(word[0], scorelist) + wordScore(word[1:], scorelist)

def wordsWithScore(dct, scores):
        """Outputs the scrabble score of each word in the list dct"""
        if dct == []:
                return []
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)

def take(n, L):
        """Returns the list L[:n]"""
        if n>len(L):
                return L
        if n == 0:
                return []
        return [L[0]] + take(n-1, L[1:])

def drop(n, L):
        """Returns the list L[n:]"""
        if n == 0:
                return L
        return drop(n-1, L[1:])
