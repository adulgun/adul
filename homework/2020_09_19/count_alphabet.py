# 22p21i0098-อดุลวิทย์
# https://github.com/adulgun/adul

import numpy as np

nameList = ['Mike', 'Winn', 'Eak', 'Non']

def count_alphabet(alphabet):
    return len(list(filter(lambda x: alphabet in x, nameList)))

print(count_alphabet(str(input("Alphabet ที่สนใจ: "))[0]))