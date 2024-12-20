class Calculator:
    def add(self, first, second):
        return first + second
    def subtract(self, first, second):
        return first - second
    def multiply(self, first, second):
        return first * second
    def divide(self, first, second):
        if second == 0:
            return "Error"
        return first / second

calc = Calculator()
first = 25
second = 5
print("calculator:")
print(calc.add(first, second))
print(calc.subtract(first, second))
print(calc.multiply(first, second))
print(calc.divide(first, second))