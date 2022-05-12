import numpy as np

x = np.array([1, 2, 3])
x.__class__
x.shape
x.ndim

W = np.array([[1, 2, 3], [4, 5, 6]])
W.shape
W.ndim

W = np.array([[1, 2, 3], [4, 5, 6]])
X = np.array([[0, 1, 2], [3, 4, 5]])
W+X
W*Y # 대응하는 원소별 곱
A*10 # 브로드캐스트

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.dot(a, b)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
np.matmul(A, B) # as it is

####################################
import numpy as np

W1 = np.random.randn(2, 4)
b1 = np.random.randn(4)
x = np.random.randn(10, 2)
h = np.matmul(x, W1) + b1
