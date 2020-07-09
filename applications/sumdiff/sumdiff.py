"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# iterate and store set into a dictionary

def Combos(orderedNumSet):
    pass
# list from L-R
a = f(1) + f(3)
# List from R-L
b = f(12) - f(7)

# compare sides 
if a == b:
    pass

if __name__ == '__main__':
    print(Combos)
    
    print("")
