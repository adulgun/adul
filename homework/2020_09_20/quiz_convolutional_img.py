# 22p21i0098-อดุลวิทย์
# https://github.com/adulgun/adul

import numpy as np
import sys
import os

def convimg(imgmat, filt):
    size_filt = filt.shape[0]
    size_row = imgmat.shape[0] - 2
    size_col = imgmat.shape[1] - 2
    result = np.zeros((size_row, size_col))
    for i in range(size_row):
        for j in range(size_col):
            result[i, j] = np.sum(imgmat[i:i+size_filt, j:j+size_filt] * filt)
    return np.array(result)

a = np.arange(20)
a = a.reshape(5, 4)
print("image:")
print(a)
b = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("filter:")
print(b)
print("sliding window:")
print(convimg(a, b))
