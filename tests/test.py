import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..')))
from super_ai.homework import *

class Test_SuperAI(unittest.TestCase):
    hw = Homework()
    def test_convimg(self):
        a = np.arange(100)
        a = a.reshape(10, 10)
        b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        result = self.hw.convimg(a, b)
        self.assertEqual(result.shape, (a.shape[0]-2, a.shape[1]-2))

    def test_count_alphabet(self):
        result = self.hw.count_alphabet('n')
        self.assertEqual(2, result)

if __name__ == "__main__":
    unittest.main()
