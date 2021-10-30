from fractions import Fraction

def mixed_numeral(vuglar):
    if not (hasattr(vuglar, 'numerator') and hasattr(vuglar, 'denominator')):
        raise TypeError("{} is not a rational number".format(vuglar))

    integer = vuglar.numerator // vuglar.denominator
    fraction = Fraction(vuglar.numerator - integer * vuglar.denominator, vuglar.denominator)

    return integer, fraction

def eafpmixed_numeral(vuglar):
    try:
        integer = vuglar.numerator // vuglar.denominator
        fraction = Fraction(vuglar.numerator - integer * vuglar.denominator, vuglar.denominator)
        return integer, fraction
    except AttributeError as e:
        raise TypeError("{} is not a rational number".format(vuglar)) from e

if __name__ == '__main__':
    input_value = input('enter a number')
    print(eafpmixed_numeral(input_value))