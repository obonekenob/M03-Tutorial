""" 
    M03 Tutorial
    Paul R.Thompson
    File name: M03Tut.py
"""

# OOP paradigm Class and methods (class name is do_math)
class do_math:

    # initialize variables in class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # subtract method
    def subnum(self):
        return self.x - self.y
    
    # floating point division method
    def divnumf(self):
        return self.x / self.y

    # integer division method
    def divnumi(self):
        return self.x // self.y

# Functional paradigm functions
# A Subtract function
def subtract(x, y):
    return (x - y)

# A Float Division function
def dividef(x, y):
    return(x / y)

# An Integer Division function
def dividei(x, y):
    return(x // y)

# Run the functions and print output

print("\nOutput from functions")
print(subtract(24, 12))
print(dividei(24, 12))
print(dividef(24, 12))

# insantiate the class
math_instance = do_math(24, 12)

# call the methods and print output

print("\nClass do_math output")
print(math_instance.subnum())
print(math_instance.divnumf())
print(math_instance.divnumi())
print("\n")
