from functools import reduce



def gauss(N):
    return (N+1)/2*N

def square(N):
    return N**2

def add(x, y):
    return x+y

def sumOfSquares(N):
    return reduce(add, map(square, range(N+1)))

print(sumOfSquares(5))
