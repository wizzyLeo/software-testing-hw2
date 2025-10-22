class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return 1000

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
