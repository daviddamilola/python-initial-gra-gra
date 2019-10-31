def fib(n):
    """
    finds the nth fibonacci number
     """
    if n <= 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def main():
   result = fib(int(input('enter an integer to rep fib number')))
   print(result)

main()
