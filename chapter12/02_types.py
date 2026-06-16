n:int=5
name:str="khusanoob"

def sum(a:int,b:int)->int:
    return(a+b)

print(sum(3,4))


from typing import List ,Tuple ,Dict ,Union

#list of  integer
numbers : list[int] =[1,2,3,4]

#tuple of a string and integer
person : tuple[str,int] =("khusanoob",30)

#dictonary of string keys and integer values
scores : dict[str,int] ={"timber":90 ,"Khusanoob":30}

#union type for variables that can hold multiple types
identifier : Union[int,str]  ="ID123"
identifier = 12345 #also valid