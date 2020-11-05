class ComplexNum:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNum(real, imag)
    

    def __str__(self):
        return f"{self.real} + ({self.imag}i)"


a = ComplexNum(1, 1)
b = ComplexNum(3, 6)

result = a.__add__(b)

print(result)
