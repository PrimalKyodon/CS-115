#################################################
#	Name: Aaren Patel
#	Date: 10/19/22
#	I pledge my honor that I have abided by the Stevens Honor System.
#	CS115 - Homework 3
#
################################################

def pascalSum(L):
    """Returns the list of the sums of two consecutive numbers"""
    if len(L) < 2:
        return []
    return [L[0] + L[1]] + pascalSum(L[1:])

def pascal_row(n):
    """Returns the nth row of Pascal's triangle"""
    if n == 0:
        return [1]
    return [1] + pascalSum(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    """Returns Pascal's triangle of size n"""
    if n == 0:
        return [[1]]
    return pascal_triangle(n-1) + [pascal_row(n)]
	
def test_pascal_row():
    """Tests pascal_row"""
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1, 2, 1]
    assert pascal_row(3) == [1, 3, 3, 1]

	
def test_pascal_triangle():
    """Tests pascal_triangle"""
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(0) == [[1]]
	
