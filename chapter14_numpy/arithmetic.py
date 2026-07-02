import numpy as np
#scalar arithemetic

array=np.array([1,2,3])

print(array+1)
print(array-2)
print(array*3)
print(array/4)
print(array**5)

#VECTORIZED math function

array=np.array([1,2,3])

print(np.sqrt(array))
print(np.round(array))
print(np.pi)

radii=np.array([1,2,3])

print(np.pi * radii**2)

#Element-wise Arthemetic
array1=np.array([1,2,3])
array2=np.array([4,5,6])

print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)

#Comparision Operator

scores=np.array([91,55,45,35,56,100])

# print(scores==100)
# print(scores>=60)
# print(scores<60)
scores[scores<60]=0
print(scores)

