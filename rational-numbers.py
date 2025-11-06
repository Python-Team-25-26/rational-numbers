from math import sqrt
from fractions import Fraction

class RationalNumbersIterator:
    def __init__(self, max_denominator=None):
        self.max_denominator = max_denominator
        self.current_denominator = 2
        self.current_numerator = 1
        self._setup_next_valid()
    
    def _has_common_divisor(self, numerator, denominator):
        if numerator == 1:
            return False
        
        if (denominator % numerator == 0):
            return True
        
        for divisor in range(2, int(sqrt(numerator)) + 1):
            if numerator % divisor == 0:
                if denominator % divisor == 0:
                    return True
                other_divisor = numerator // divisor
                if other_divisor > 1 and denominator % other_divisor == 0:
                    return True
        return False
    
    def _setup_next_valid(self):
        while True:
            if self.current_numerator is None:
                return
            
            if self.current_numerator >= self.current_denominator:
                self.current_denominator += 1
                self.current_numerator = 1
                if self.max_denominator and self.current_denominator > self.max_denominator:
                    self.current_numerator = None
                    return
                
            if not self._has_common_divisor(self.current_numerator, self.current_denominator):
                return
            
            self.current_numerator += 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_numerator is None:
            raise StopIteration
        
        result = Fraction(self.current_numerator, self.current_denominator)
        
        self.current_numerator += 1
        self._setup_next_valid()
        
        return result

if __name__ == "__main__":
    for i in RationalNumbersIterator(6):
        print(i, end=" ")