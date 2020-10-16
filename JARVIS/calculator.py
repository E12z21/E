import math


class Calc(object):
    def __init__(self):
        pass
    def add(self, num1, num2):
        return float(num1) + float(num2)

    def subtract(self, num1, num2):
        return float(num1) - float(num2)

    def multiply(self, num1, num2):
        return float(num1) * float(num2)

    def divide(self, num1, num2):
        return float(num1) / float(num2)

    def computePowers(self, num1, num2):
        return float(num1) ** float(num2)

    def get_pi(self):
        return float(math.pi)

    def get_e(self):
        return float(math.e)

    def computeLogs(self, num1, num2):
        return float(math.log(float(num2), float(num1)))

    def computeFactorials(self, num):
        return float(math.factorial(float(num)))

    def sin(self, num):
        return float(math.sin(float(num)))

    def cos(self, num):
        return float(math.cos(float(num)))

    def tan(self, num):
        return float(math.tan(float(num)))

