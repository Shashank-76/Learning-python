s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
print(s)#python evaluates 20 and 20.0 as the same value,
# so only one of them is added to the set. 
# The string '20' is considered a different value,
# so it is also added to the set. 
# Therefore, the length of the set is 2 and it contains the
# values {20, '20'}.