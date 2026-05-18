import math

import app


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise TypeError("User has no permissions")

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        try:
            return math.pow(x, y)
        except (ValueError, OverflowError) as e:
            raise TypeError("Invalid parameters for power") from e

    def sqrt(self, x):
        self.check_number(x)
        if x < 0:
            raise TypeError("Square root is only defined for non-negative numbers")

        return math.sqrt(x)

    def log10(self, x):
        self.check_number(x)
        if x <= 0:
            raise TypeError("Logarithm base 10 is only defined for positive numbers")

        return math.log10(x)

    @staticmethod
    def check_types(x, y):
        Calculator.check_number(x)
        Calculator.check_number(y)

    @staticmethod
    def check_number(value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Parameters must be numbers")

        if not math.isfinite(value):
            raise TypeError("Parameters must be finite numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
