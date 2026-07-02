import numpy as np
print(np.__version__)

array=np.array('A')
print(array.ndim)

array=np.array([['A','B','C'],
                ['D','E','F'],
                ['G','H','I']])
print(array.ndim)

array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                [['J','K','L'],['M','N','O'],['P','Q','R']],
                [['S','T','U'],['V','W','X'],['Y','Z','']]])
print(array.ndim)
print(array.shape)
array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                [['J','K','L'],['M','N','O'],['P','Q','R']],
                [['S','T','U'],['V','W','X'],['Y','Z','']]])

#chain indexing
print(array[0][0][0])
#multidimensional indexing
print(array[0,0,0])
word=array[0,0,0]+array[2,0,0]+array[2,0,0]
print (word)