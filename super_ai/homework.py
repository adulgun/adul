import numpy as np
import numbers

class Homework():
    def __init__(self):
        self.nameList = ['Mike', 'Winn', 'Eak', 'Non']

    def count_alphabet(self, alphabet):
        return len(list(filter(lambda x: alphabet in x, self.nameList)))

    def convimg(self, imgmat, filt):
        size_filt = filt.shape[0]
        size_row = imgmat.shape[0] - 2
        size_col = imgmat.shape[1] - 2
        result = np.zeros((size_row, size_col))
        for i in range(size_row):
            for j in range(size_col):
                result[i, j] = np.sum(imgmat[i:i+size_filt, j:j+size_filt] * filt)
        return np.array(result)

    def maximum_number(self, numberList):
        return np.max(np.array(list(filter(lambda x: isinstance(x, numbers.Number), numberList))))

    def depth_first_search(self, graph, source):
        path = []
        stack = [source]
        while(len(stack) != 0):
            s = stack.pop()
            if s not in path:
                path.append(s)
            if s not in graph:
                continue
            for neighbor in graph[s]:
                stack.append(neighbor)
        return path