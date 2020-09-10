#import decimal
from decimal import Decimal as d
print(d(0.1))
print(d(2.2)+d(1.1))
import fractions
print(fractions.Fraction(1.5))
print(fractions.Fraction(1,5))
a=fractions.Fraction(1.1)
print(type(a))
b=fractions.Fraction('1.1')
print(type(b))
