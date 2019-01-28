import unittest
import calc


class CalcBasicTests(unittest.TestCase):
    @unittest.skip("Сброшен тест - test_add")
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(4, 2), 2)

    def test_mult(self):
        self.assertEqual(calc.mult(5, 2), 10)

    def test_div(self):
        self.assertEqual(calc.div(81, 9), 3)


@unittest.skip('Сброшен тест - CalcExTests')
class CalcExTests(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(2), 4)

    def test_pow(self):
        self.assertEqual(calc.pow(1, 2), 3)


if __name__ == "__main__":
    pass