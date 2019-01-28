import unittest


class TestRepetitiveCode(unittest.TestCase):
    def setUp(self):
        self.var= -10

    def test_absolute(self):
        self.assertEqual(self.var, -10)

    def test_overwrite(self):
        self.var = -10
        self.assertTrue(self.var < 0)


def suite():
    Suite = unittest.TestSuite()
    unittest.main(TestRepetitiveCode('test_absolute'))
    unittest.main(TestRepetitiveCode('test_overwrite'))
    return Suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
