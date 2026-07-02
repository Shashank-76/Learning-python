import numpy as np

#broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions so they match the larger arrays shape.
#the dimension have the same size. OR one of the dimension has the size of 1.

array1= np.array([[1,2,3,4]])
array2= np.array([[1],[2],[3],[4]])
print(array1.shape)
print(array2.shape)

print(array1*array2)

array1= np.array([[1,2,3,4]
                  [5,6,7,8]])
array2= np.array([[1],[2],[3],[4]])
print(array1.shape)
print(array2.shape)

print(array1*array2)