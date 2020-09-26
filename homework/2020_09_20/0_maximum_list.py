# 22p21i0098-อดุลวิทย์
# https://github.com/adulgun/adul

import random
import numpy as np
import numbers

def maximum_number(numberList):
        return np.max(np.array(list(filter(lambda x: isinstance(x, numbers.Number), numberList))))

a = np.array(np.random.randint(100, size=[100]))
print("number of list:")
print(a)
print("Maximum:")
print(maximum_number(a))