import numpy as np
 
#   integer
rng=np.random.default_rng(seed=1)# SEED IS USED TO REPRODUCE THE SAME RESULT IF WE DONT SET SEED NUMPY WILL SET IT FOR US

print(rng.integers(low=1,high=101,size=(5,4)))

# floating number
np.random.seed(seed=2)
print(np.random.uniform(low=-1,high=5,size=(3,2)))

#suffle an array
rng=np.random.default_rng()
array=np.array ([1,2,4,5,7])
rng.shuffle(array)
print(array)

#for random choice
rng=np.random.default_rng()
fruits=(['🍎','🍌','🍇','🥭','🍍'])
fruit=rng.choice(fruits,size=(4,4))
print(fruit)