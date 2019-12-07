import numpy as np
def sigmoid (x):
 return 1/(1 + np.exp(-x))

def derivatives_sigmoid(x):
 return x * (1 - x)

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
X = X/np.amax(X,axis=0) # maximum of X array longitudinally
y = y/100

alpha,hidden_dim = (0.05,3)
synapse_0 = 2*np.random.random((2,hidden_dim)) - 1
synapse_1 = 2*np.random.random((hidden_dim,1)) - 1
layer_2 = np.empty_like(y)
for j in range(60000):
    layer_1 = np.tanh(np.dot(X,synapse_0))
    layer_2 = sigmoid(np.dot(layer_1,synapse_1))
    layer_2_delta =  (layer_2 - y) * derivatives_sigmoid(layer_2)
    layer_1_delta = layer_2_delta.dot(synapse_1.T) * derivatives_sigmoid(layer_1)
    synapse_1 -= (alpha * layer_1.T.dot(layer_2_delta))
    synapse_0 -= (alpha * X.T.dot(layer_1_delta))
print(y)
print(layer_2)