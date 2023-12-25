# import pandas as pd
# from scipy import sparse
import numpy as np
# from scipy.sparse import csr_matrix

# arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

# print(csr_matrix(arr))

# json = pd.read_json('./../test.json')
# x = np.array(json['age'])

from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.eliminate_zeros()
mat.sum_duplicates()
print(mat)
