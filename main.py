import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real_part = (self.real * no.real) - (self.imaginary * no.imaginary)
        imaginary_part = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(real_part, imaginary_part)

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        conjugate_real = no.real / denominator
        conjugate_imaginary = -no.imaginary / denominator
        numerator = self.__mul__(Complex(conjugate_real, conjugate_imaginary))
        return Complex(numerator.real, numerator.imaginary)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.real == 0 and self.imaginary == 0:
            return "0.00+0.00i"
        elif self.real == 0:
            return "{:.2f}{:+.2f}i".format(self.imaginary, 0.00)
        elif self.imaginary == 0:
            return "{:.2f}+0.00i".format(self.real)
        else:
            return "{:.2f}{:+.2f}i".format(self.real, self.imaginary)

if __name__ == '__main__':
    c = list(map(float, input().split()))
    d = list(map(float, input().split()))
    x = Complex(*c)
    y = Complex(*d)

    result_addition = x + y
    result_subtraction = x - y
    result_multiplication = x * y
    result_division = x / y
    result_mod_x = x.mod()
    result_mod_y = y.mod()

    print(result_addition)
    print(result_subtraction)
    print(result_multiplication)
    print(result_division)
    print(result_mod_x)
    print(result_mod_y)
