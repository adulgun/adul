from super_ai.homework import *
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..')))

hw = Homework()

a = np.arange(20)
a = a.reshape(5, 4)
print("image:")
print(a)
b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("filter:")
print(b)
print("sliding window:")
print(hw.convimg(a, b))
