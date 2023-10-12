####################################################################
#   Aaren Patel and Eric Zhu
#   10/31/22
#   I pledge my honor that I have abided by the Stevens Honor System
#   CS 115 - HW 6
####################################################################
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBin(n):
    """Converts the base10 input to binary"""
    if n == 0:
        return ""
    return numToBin(n // 2) + str(n % 2)

def binToNum(S):
    """Converts the binary input to base10"""
    if S == "":
        return 0
    return binToNum(S[1:]) + int(S[0])*2**(len(S)-1)

def count(S):
    """Returns the count of consecutive digits - 1 in binary format"""
    if len(S) == 1 or S[0] != S[1]:
        return 1
    return 1 + count(S[1:])

def doCompress(S):
    """Compresses S based on the number of consecutive 1's and 0's into a binary count format"""
    if S == "":
        return ""
    if count(S) > MAX_RUN_LENGTH:
        return "1" * COMPRESSED_BLOCK_SIZE + "0" * COMPRESSED_BLOCK_SIZE + doCompress(S[MAX_RUN_LENGTH:])
    return (COMPRESSED_BLOCK_SIZE - len(numToBin(count(S)))) * "0" + numToBin(count(S)) + doCompress(S[count(S):])
            
def compress(S):
    """Returns the compressed string S using run-length-encoding"""
    if S == "":
        return ""
    if S[0] == "1":
        return "0" * COMPRESSED_BLOCK_SIZE + doCompress(S)
    return doCompress(S) 

def uncompress(S): 
    """Returns the compressed string input back in its original 1/0 orientation"""
    if S == "":
        return ""
    string0 = binToNum(S[:COMPRESSED_BLOCK_SIZE]) * "0"
    if len(S) == COMPRESSED_BLOCK_SIZE:
        return string0
    return string0 + binToNum(S[COMPRESSED_BLOCK_SIZE:COMPRESSED_BLOCK_SIZE * 2]) * "1" + uncompress(S[COMPRESSED_BLOCK_SIZE*2:])

def compression(S):
    """Returns the ratio of the compressed string to the regular string"""
    return len(compress(S))/len(S)

Penguin = "00011000" + "00111100" * 3 + "01111110" + "11111111" + "00111100" + "00100100"
print("Penguin = " + Penguin + "; " + str(compression(Penguin)) + "; " + compress(Penguin))
Smile = "0" * 8 + "01100110" * 2 + "0" * 8 + "00001000" + "01000010" + "01111110" + "0" * 8
print("Smile = " + Smile + "; " + str(compression(Smile)) + "; " + compress(Smile))
Five = "1" * 9 + "0" * 7 + "10000000" * 2 + "1" * 7 + "0" + "00000001" * 2 + "1" * 7 + "0"
print("Five = " + Five + "; " + str(compression(Five)) + "; " + compress(Five))

"""
Questions:
    1. The max number of bits to store a 64-bit image is (64 + 1) * COMPRESSED_BLOCK_SIZE because if you alternate between 1's and 0's the code will need a number of bits equal to COMPRESSED_BLOCK_SIZE for each bit in the image. If you start with a 1 you need an additional 5 bits to let the computer know to start with 1's as it defaults to starting with 0's.

    2. [Penguin = 1.484375, Smile = 1.328125, Five = 1.015625]

S; compression(S); compress(S)

Penguin = 0001100000111100001111000011110001111110111111110011110000100100; 1.484375;
00011000100010100100001000010000100001000001100110000010100000010001000010000001000100000100010

Smile = 0000000001100110011001100000000000001000010000100111111000000000; 1.328125;
0100100010000100001000010000100001000010011010000100100000010010000001000100011001001

Five = 1111111110000000100000001000000011111110000000010000000111111110; 1.015625;
00000010010011100001001110000100111001110100000001001110100000001

    3. There is no way to differentate between whether the string is then in relation to the compressed form or the original format so the computer when uncompressing won't be able to tell the difference between the normal or compressed string input and produce wrong output. 
"""
