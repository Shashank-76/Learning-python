class twoD_vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f'Thw vectors are {self.i}i + {self.j}j')
        
class threeD_vector(twoD_vector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f'Thw vectors are {self.i}i + {self.j}j + {self.k}k')
        
a=twoD_vector(2,3)
a.show()

b=threeD_vector(4,4,6)
b.show()