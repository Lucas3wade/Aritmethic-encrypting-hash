def arithmetic_example(first_number, second_number, modulo):
    first_number = Arithmetic(first_number, modulo)
    second_number = Arithmetic(second_number, modulo)

    addition = first_number.__add__(second_number)
    subtraction = first_number.__sub__(second_number)
    multiplication = first_number.__mul__(second_number)

    inverse_first = first_number.inverse()
    inverse_second = second_number.inverse()

    print("Addition: ", addition.__str__())
    print("Subtraction:", subtraction.__str__())
    print("Multiplication: ", multiplication.__str__())

    print("First inverse: ", inverse_first.__str__())
    print("Second inverse: ", inverse_second.__str__(), '\n')


class Arithmetic:

    def __init__(self, value, modulo):
        self.__modulo = modulo
        self.__value = value % modulo

    def __add__(self, other):
        new_value = (self.__value + other.__value) % self.__modulo
        return Arithmetic(new_value, self.__modulo)

    def __sub__(self, other):
        new_value = (self.__value - other.__value) % self.__modulo
        return Arithmetic(new_value, self.__modulo)

    def __mul__(self, other):
        new_value = (self.__value * other.__value) % self.__modulo
        return Arithmetic(new_value, self.__modulo)

    def __str__(self):
        return str(self.__value)

    # inverse modulo: a*a^-1 = 1 (mod m)
    def inverse(self):
        m = self.__modulo
        a = self.__value
        m0 = m
        y = 0
        x = 1

        if m == 1:
            return 0

        while a > 1:
            q = a // m
            t = m
            m = a % m
            a = t
            t = y
            y = x - q * y
            x = t

        if x < 0:
            x = x + m0

        return Arithmetic(x, self.__modulo)
