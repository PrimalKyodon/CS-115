##############################################
#   Name: Aaren Patel
#   Date: 9/29/22
#   CS 115 Lab 3
#   I pledge my honor that I have abided by the Stevens Honor System.
#
##############################################
from functools import reduce

def change(amount, coins):
    """Returns the minimum number of coins of the denominations listed in coins to make the value amount"""
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0]>amount:
        return change(amount, coins[1:])
    else:
        use = 1 +  change((amount-coins[0]), coins)
        lose = change(amount, coins[1:])
        return min(use, lose)


