import unittest
import test_for_calc


calcTestSuie = unittest.TestSuite()
calcTestSuie.addTest(unittest.makeSuite(test_for_calc.CalcBasicTests))
calcTestSuie.addTest(unittest.makeSuite(test_for_calc.CalcExTests))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuie)
