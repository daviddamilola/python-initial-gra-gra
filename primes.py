
from math import sqrt

def isPrime(n):
    """
    determimes the primality of n
    n is an integer to test for primality
    returns true if n is prime otherwise false

    """
    root = round(sqrt(n)) +1
    for trial_factor in range(2, root):
        if n % trial_factor == 0:
            return False
        return True


def erasthosthenesSive(n):
    """
    Generates all the prime numbers from 2 to n - 1.
    n - 1 is the largest potential prime considered.
    Algorithm originally developed by Eratosthenes.
    """
    nonPrimes = n * [False]
    count = 0
    nonPrimes[0] = nonPrimes[1] = True;

    for i in range(2, n):
        if not nonPrimes[i]:
            count += 1
            for j in range(2*i, n, i)
            nonPrimes[j] = True


def prime_sequence(begin, end):
    """ Generates the sequence of prime numbers between begin and end. """
    for value in range(begin, end + 1):
        if is_prime(value):
            yield value

            
def main():
    """
    tests for primality of an integer entered by a user
    """
    max_value = int(input('show primes up to what'))
    for value in range(2, max_value+1):
        if isPrime(value):
            print(value, end=" ")
        print()

main()
