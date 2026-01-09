import pytest
from src.calculator import Calculator


class TestCalculatorIntegration:

    def test_add_sub_mul_flow(self):
        """
        add → sub → mul flow
        """
        calc = Calculator()

        add_result = calc.add(10, 20, 30)     # 60
        sub_result = calc.sub(add_result, 10) # 50
        mul_result = calc.mul(sub_result, 2)  # 100

        assert mul_result == 100

    def test_negative_numbers_flow(self):
        """
        Integration test with negative values
        """
        calc = Calculator()

        add_result = calc.add(-5, -5)         # -10
        sub_result = calc.sub(add_result, -5) # -5
        mul_result = calc.mul(sub_result, -2) # 10

        assert mul_result == 10

    def test_shared_validation_across_methods(self):
        """
        Validation should work the same for all methods
        """
        calc = Calculator()

        with pytest.raises(TypeError):
            calc.add(1, 2, "x")

        with pytest.raises(TypeError):
            calc.sub(10, "y")

        with pytest.raises(TypeError):
            calc.mul(3, "z")

    def test_single_value_flow(self):
        """
        Single value should pass through all operations
        """
        calc = Calculator()

        value = calc.add(10)
        value = calc.sub(value)
        value = calc.mul(value)

        assert value == 10
