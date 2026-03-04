import unittest

def suma(a, b):
    return a + b

class TestBasico(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 2), 4)

if __name__ == '__main__':
    unittest.main()
