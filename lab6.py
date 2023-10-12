#####################################################################
#   Name: Aaren Patel
#   I pledge my honor that I have abided by the Stevens Honor System.
#   CS 115 - Lab 6
#   10/20/22
#
#####################################################################

def isOdd(n):
    """Returns whether or not the integer argument is odd"""
    return n%2!=0
"""
Next you go to the next multiple of 2 which is 8. Since 8 goes into 10 we have '1' and 10-8=2 remaining. Then we move to 4. Since 4>2 we have a '0'. Then we move to 2. Since 2=2 we have a one and the remaining digits are 0. 101010

"""
def numToBinary(n):
    """Returns the string with the binary representation of non-negative integer n."""
    if n == 0:
        return ""
    if isOdd(n):
        return numToBinary(n//2) + "1"
    return numToBinary(n//2) + "0"
"""
An odd base 10 number's last digit in binary is one and an even number's is 1

The original  value is right shifted so it is integer divided by 2

Given the base10 representation of Y if N is odd the base10 representation of N is Base10(Y)*2 + 1 and if N is even its just Base10(Y)*2

"""
def binaryToNum(s):
    """Returns the integer corresponding to the binary representation in s"""
    if s == "":
        return 0
    return binaryToNum(s[1:]) + int(s[0])*2**(len(s)-1)

def increment(s):
    """Returns the binary representation of binaryToNums(s)+1"""
    if s == "":
        return ""
    if s[-1] == "1":
        return increment(s[:-1]) + "0"
    return s[:-1] + "1"

def count(s, n):
    """Prints s and its n successors""" 
    print(s)
    if n != 0:
        count(increment(s), n-1)

def numToTernary(n):
    """Returns the string with the ternary representation of non-negative integer n."""
    if n == 0:
        return ""
    return numToTernary(n//3) + str(n%3)
"""
59 in ternary is 59%3='2'. 59//3=19. 19%3='1'. 19//3=6. 6%3='0'. 6//3=2. 2%3='2'. Base10(59) = Base3(2102)

"""
def ternaryToNum(s):
    """Returns the integer corresponding to the ternary representation in s."""
    if s == "":
        return 0
    return ternaryToNum(s[1:]) + int(s[0])*3**(len(s)-1)

