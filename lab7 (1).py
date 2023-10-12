#####################################################################
#   Aaren Patel
#   I pledge my honor that I have abided by the Stevens Honor System
#   10/26/22
#   CS 115 - Lab 7
#####################################################################    

def gnot(x):
    """Tests the not gate"""
    assert x in [0, 1]
    return int(not(x)) 

def gand(x, y):
    """Tests the and gate"""
    assert x in [0, 1] and y in [0, 1]
    return x and y

def gor(x, y):
    """Tests the or gate"""
    assert x in [0, 1] and y in [0, 1]
    return x or y

def XOR(x, y):
    """Returns True if only x or if only y is True"""
    return gor(gand(gnot(x), y), gand(x, gnot(y)))

def testXOR():
    """Tests the xor gate"""
    assert XOR(0, 0) == 0
    assert XOR(0, 1) == 1
    assert XOR(1, 0) == 1
    assert XOR(1, 1) == 0
    print("testXOR success")

def gor3(x, y, z):
    """Runs the or gate on the three inputs: Returns True as long as one input is true"""
    return gor(x, gor(y, z))

def FA(x, y, cin):
    """Return the pair of bits (carry_out, sum) such that sum is the low bit of x + y + cin and carry_out is the high bit of x + y + carry_in."""
    return (gor(gand(x,y), gand(cin, XOR(x,y))), XOR(XOR(x, y), cin))

            
def FAtest(x, y, c):
    """Compute FA using integer arithmetic."""
    s = (x + y + c) % 2
    d = 1 if x + y + c >= 2 else 0
    return (d, s)

def testFA():
    """Tests FA"""
    assert FA(0, 0, 0) == FAtest(0, 0, 0) 
    assert FA(0, 1, 0) == FAtest(0, 1, 0) 
    assert FA(1, 1, 1) == FAtest(1, 1, 1)
    print("testFA successful on 3 out of 8 cases")

def twoBitAdd(xx, yy):
    """Return (cout, (zt, zo)) where (zt, zo) is their two-bit sum is the carry bit."""
    (c, zo) = FA(xx[1], yy[1], 0) 
    (d, zt) = FA(xx[0], yy[0], c)
    return (d, (zt, zo))

def test_twoBitAdd():
    """Tests twoBitAdd"""
    zero = (0, 0)
    one = (0, 1)
    two = (1, 0)
    three = (1, 1)
    c, ww = twoBitAdd(one, zero)
    assert(ww == (0, 1) and c == 0)
    c, ww = twoBitAdd(one, one)
    assert(ww == (1, 0) and c == 0)
    c, ww = twoBitAdd(three, three)
    assert(ww == (1, 0) and c == 1)
    print("test_twoBitAdd worked (but incomplete test)")

def fourBitAdd(xxxx, yyyy):
    """Return (c, zzzz) where zzzz is their four-bit sum
    and c is the carry."""
    (c1, zo) = FA(xxxx[3], yyyy[3], 0)
    (c2, zt) = FA(xxxx[2], yyyy[2], c1)
    (c3, zf) = FA(xxxx[1], yyyy[1], c2)
    (c4, ze) = FA(xxxx[0], yyyy[0], c3)
    return (c4, (ze, zf, zt, zo))

def test_fourBitAdd():
    """Tests fourBitAdd"""
    assert (fourBitAdd((1, 0, 0, 1), (0, 1, 1, 0) == (0, (1, 1, 1, 1))))
    assert (fourBitAdd((1, 1, 1, 1), (0, 1, 1, 0) == (1, (0, 1, 0, 1))))
    assert (fourBitAdd((1, 0, 0, 1), (0, 0, 1, 1) == (0, (1, 1, 0, 0))))
    assert (fourBitAdd((1, 1, 1, 1), (1, 1, 1, 1) == (1, (1, 1, 1, 0))))
    
    
