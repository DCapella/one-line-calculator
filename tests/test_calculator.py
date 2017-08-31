from one_line_calculator import calculator

def get_expression(string):
    calculator.input = lambda *args: string
    expression = calculator.expression()
    output = calculator.calculate(expression)
    return output

class TestClass(object):
    def test_expression(self):
        """Remove spacing"""
        calculator.input = lambda *args: ' space space '
        output = calculator.expression()
        assert output == 'spacespace'

    def test_expression_two(self):
        """Checking for correct expression"""
        calculator.input = lambda *args: ' 1 + 2 '
        output = calculator.expression()
        assert output == '1+2'

    def test_calculate(self):
        """Addition correctly"""
        output = get_expression(' 1 + 2 ')
        assert output == 3

    def test_calculate_multiply(self):
        """multiplication correctly"""
        output = get_expression(' 4 * 2')
        assert output == 8

    def test_calculate_multiply_x(self):
        """multiplication with x"""
        output = get_expression('4x2')
        assert output == 8

    def test_calculate_multiply_X(self):
        """multiplication with X"""
        output = get_expression('4 X 2')
        assert output == 8

    def test_calculate_division(self):
        """division correctly"""
        output = get_expression('4 / 2')
        assert output == 2

    def test_calculate_power(self):
        """Power with ^"""
        output = get_expression('2^3')
        assert output == 8

    def test_calculate_power_star(self):
        """Power with **"""
        output = get_expression('2**3')
        assert output == 8

    def teardown_method(self, method):
        """
        This method is being called after each test case, and it will revert
        input back to original function
        """
        calculator.input = input
