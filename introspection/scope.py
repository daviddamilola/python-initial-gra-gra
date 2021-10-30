def report_scope(arg):
    name= 'david'
    age= 23
    country = 'Nigeria'
    from pprint import pprint as pp
    x = 496
    pp(locals(), width=10)
    pp("{name} is {age} years old from {country}".format(**locals()))

if __name__ == '__main__':
    report_scope(42)