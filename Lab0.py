############################################################
# Name: Aaren Patel
# Pledge: I Pledge My Honor That I Have Abided By The Stevens Honor System
# CS115 Lab 0
#  
############################################################



def same(word):
#Input: String Output: Bool comparing the first and last letters of the input String(Case-insensitive)
    lowerWord = word.lower()
    return lowerWord[0] == lowerWord[-1]

    
def consecutiveSum(x, y):
#returns the sum of the values between the two inputted integers
    return ((y+x)/2)*(y-x-1)
        

