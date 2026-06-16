l= [23,344,5,6,36,7]

index=0
for item in l:
    print(f'The item number at index {index} is {item}')
    index+=1

#this can be simplified using enumerate function

for index,item in enumerate(l):
     print(f'The item number at index {index} is {item}')