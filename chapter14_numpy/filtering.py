# filtering refers to the process of selecting elements from a array that match the given condition
import numpy as np
ages=np.array([[23,21,22,24,19,18,17,16,63],
               [16,18,18,93,84,54,55,34,23]])

teenagers=ages[ages<18]
adults=ages[(ages>=18)&(ages<60)]
seniors=ages[ages>=60]
evens=ages[ages%2==0]
odds=ages[ages%2!=0]
 
print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds) 

#to preserve the origanl shape

adults=np.where(ages>=18,ages,0)

print(adults)