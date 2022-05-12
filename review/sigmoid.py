#import numpy as np

def sigmoid(x):
  return 1/(1+np.exp(-x))

import numpy as np

x = np.random.randn(10, 2)
W1 = np.random.randn(2, 4)
b1 = np.random.randn(4)
W2 = np.random.randn(4, 3)
b2 = np.random.randn(3)

h = np.matmul(x, W1) + b1
a = sigmoid(h)
s = np.matmul(a, W2) + b2



#########################
# coding: utf-8
import numpy as np

class Sigmoid:
  def __init__(self):
    self.params = []
   
  def forward(self, x):
    return 1/ (1+np.exp(-x))
  
class Affine:
  def __init__(self, W, b):
    self.params = [W, b]
   
  def forward(self, x):
    W, b = self.params
    out = np.matmul(x, W) + b
    return out
  
class TwoLayerNet:
  def __init__(self, input_size, hidden_size, output_size):
    I, H, O = input_size, hidden_size, output_size
    
    # initialize weight and bias
    W1 = np.random.randn(I, H)
    b1 = np.random.randn(H)
    W2 = np.random.randn(H, O)
    b2 = np.random.randn(O)
    
    # make class( = status)
    self.layers = [
      Affine(W1, b1),
      Sigmoid(),
      Affine(W2, b2)
    ]
    
    self.params = []
    for layer in self.layers
      self.params += layer.params
      
  def predict(self, x): # inference
    for layer in self.layers:
      x = layer.forward(x)
    return x

x = np.random.randn(10, 2)
model = TwoLayerNet(2, 4, 3)
s = model.predict(x)
print(s)
