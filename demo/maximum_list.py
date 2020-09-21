import sys
import os
import random
import numpy as np

sys.path.append(os.path.abspath(os.path.join('..')))
from super_ai.homework import *

hw = Homework()

a = np.array(np.random.randint(100, size=[100]))
print("number of list:")
print(a)
print("Maximum:")
print(hw.maximum_number(a))