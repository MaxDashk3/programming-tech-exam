import unittest
import arithmetic_progression_sum as app

class AppTests(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(12, app.calculate(3))
        self.assertEqual(10, app.calculate(4))

    def Teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()
