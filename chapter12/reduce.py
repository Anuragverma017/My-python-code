from    functools import reduce

l=[1,55,22,333,453,3453,234,234]

def gratest(a,b):
    if a>b:
        return a
    return b

print(reduce(gratest, l))