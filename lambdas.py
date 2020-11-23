### lambda expressions are anonymous functions in python
# form is lambda parameterlist(comma separated parameter list): expression (single python expression, cannot be a block or complete expression)
# consider for example an evaluate fn

def evaluate(fn, a, b):
    return fn(a, b)

#calling with a lambda expression

#lambda multiply fn
evaluate(lambda a, b: print(a * b), 2, 3)

#lambda print 10 if args are equivaleent
evaluate(lambda a, b: print(10 if a == b else 2), 5, 5)

#lambda functions form a closure
#A closure is a function that can capture the context of its surrounding environment.