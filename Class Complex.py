import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return complex(self.real + no.real, self.imaginary + no.imag)

    def __sub__(self, no):
        return complex(self.real - no.real, self.imaginary - no.imag)

    def __mul__(self, no):
        return complex(self.real * no.real - self.imaginary * no.imag, self.real * no.imag + self.imaginary * no.real)

    def __truediv__(self, other):
        try:
            return self.__mul__(complex(other.real, -1 * other.imag)).__mul__(complex(1.0 / (other.mod().real) ** 2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None

    def mod(self):
        return complex(pow(self.real ** 2 + self.imaginary ** 2, 0.5), 0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')