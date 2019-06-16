from app import calculator


class TestCalculator:
    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 5 == calculator.subtract(10, 5)

    def test_multiplication(self):
        assert 16 == calculator.multiplication(4, 4)

    def test_division(self):
        assert 10 == calculator.division(100, 10)
