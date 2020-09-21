import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..')))
from super_ai.homework import *

hw = Homework()

print(hw.count_alphabet(str(input("Alphabet ที่สนใจ: "))[0]))