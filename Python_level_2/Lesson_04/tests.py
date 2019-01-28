import unittest


def sum_kv_ij(i, j):
    return i * i + j * j


class TestSumIJ(unittest.TestCase):
    def testequal(self):
        self.assertEqual(sum_kv_ij(2, 3), 23)


if __name__ == "__main__":
    unittest.main()
