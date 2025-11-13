from math import sqrt
from fractions import Fraction

def _has_common_divisor(numerator, denominator):
    if numerator == 1:
        return False
    
    if denominator % numerator == 0:
        return True
    
    for divisor in range(2, int(sqrt(numerator)) + 1):
        if numerator % divisor == 0:
            if denominator % divisor == 0:
                return True
            other_divisor = numerator // divisor
            if other_divisor > 1 and denominator % other_divisor == 0:
                return True
    return False

def rationalNumbersGenerator(max_denominator=None):
    current_denominator = 2
    current_numerator = 1
    
    while True:
        if current_numerator is None:
            return
        
        if max_denominator and current_denominator > max_denominator:
            return
        
        if current_numerator >= current_denominator:
            current_denominator += 1
            current_numerator = 1
            continue
        
        if not _has_common_divisor(current_numerator, current_denominator):
            yield Fraction(current_numerator, current_denominator)
        
        current_numerator += 1

if __name__ == "__main__":
    for i in rationalNumbersGenerator(10):
        print(i, end=" ")