def maxRange(a,b,c):
    range = max([a+b-1,a+c-1,b+c-1])
    return range


print(maxRange(2,3,4))
