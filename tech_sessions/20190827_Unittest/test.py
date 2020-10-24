import unittest


def summ(a, b):

    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise Exception('STOP! Must be an integer')


def power(a, b):

    if isinstance(a, int) and isinstance(b, int):
        return a ** b
    raise Exception('STOP! Must be an integer')


def subtraction(a, b, c):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        return a - b - c
    raise Exception('STOP! Must be an integer')


class MyTestCase(unittest.TestCase):

    def testSumm(self):
        self.assertEqual(2 + 1, summ(2, 1))
        self.assertRaises(Exception, summ, 'a', 'b')
        self.assertRaises(Exception, summ, 1, 'b')
        self.assertRaises(Exception, summ, 'a', 2)
        self.assertRaises(Exception, summ, None, 2)
        self.assertRaises(Exception, summ, ['a', 'c'], 2)

    def testPower(self):
        self.assertEqual(2 ** 1, power(2, 1))
        self.assertEqual(-1 ** 1, power(-1, 1))
        self.assertEqual(1 ** -1, power(1, -1))
        self.assertRaises(Exception, power, 'a', 'b')
        self.assertRaises(Exception, power, 1, 'b')
        self.assertRaises(Exception, power, 'a', 2)
        self.assertRaises(Exception, power, None, 2)
        self.assertRaises(Exception, power, ['a', 'c'], 2)

    def testSubtraction(self):
        self.assertEqual(2 - 1 - 0, subtraction(2, 1, 0))
        self.assertEqual(1 - 1 - 1, subtraction(1, 1, 1))
        self.assertEqual(0 - 100 - 3, subtraction(0, 100, 3))
        self.assertRaises(Exception, subtraction, 'a', 'b', 'c')
        self.assertRaises(Exception, subtraction, 1, 2, 'b')
        self.assertRaises(Exception, subtraction, 'a', 2, 3)
        self.assertRaises(Exception, subtraction, None, 2, 5)
        self.assertRaises(Exception, subtraction, ['a', 'c'], 2, {'good': 'dog'})


if __name__ == "__main__":
    unittest.main()










