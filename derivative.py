""" 
formula for the derivative of a function

f′(a) = lim f(a+h)− f(a) / h
        h→0
"""

def derivative(f, h):
    return lambda x: (f(x + h) - f(x)) / h

