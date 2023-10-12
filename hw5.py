#####################################################################
#   Aaren Patel
#   I pledge my honor that I have abided by the Stevens Honor System.
#   10/24/2022
#   CS115 - Hw 5 
#####################################################################

memoL = {0: 2, 1: 1}
def fast_lucas(n):
    """Returns the nth Lucas number with memoization"""
    if n in memoL:
        return memoL[n]
    memoL[n-1] = fast_lucas(n-1)
    memoL[n-2] = fast_lucas(n-2)
    return memoL[n-1] + memoL[n-2]
    
memoC = {0: 0}
def fast_change(amount, coins):
    """Returns the number of coins required to total the given amount with memoization"""
    if amount in memoC:
        return memoC[amount]
    if coins == []:
        return float("inf")
    if coins[0]>amount:
        return fast_change(amount, coins[1:])
    use = fast_change(amount-coins[0], coins) + 1
    lose = fast_change(amount, coins[1:])
    memoC[amount] = min(use, lose)
    return memoC[amount]

print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))
