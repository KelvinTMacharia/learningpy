"""
functions are groups of related statements that perform a specific task.
1. Predefined functions e.g print, range, len
2. user - defined function

in python, a function is declared using a def keyword., followed by an identifier(use the rule of naming variables and functions.

"""

def  SaySomething():
    """
    This function prints out a statement"""
    print(" A function has been created.")

# to use above function,we call our function
SaySomething()

# A function that takes in parameters
def addNumbers(x,y):
    if x==y:
        print("Numbers are the same, use unique numbers")
    else:
        print(x+y)
addNumbers(2,2)

addNumbers(2,5)


