###
#code to compute square root of a given input by a user
###

val = float(input('enter a number to find square root'))
root = 1.0

diff = root*root - val

while diff > 0.00000001 or diff < -0.00000001:
    print(root, 'squared is', root*root)
    root =( root + val/root)/2
    diff = root*root - val
print( 'square root of', val, '=', root )
