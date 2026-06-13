from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")

    def get_status(self):
        print(f"Train no {self.trainNo} is running on time")
        
    def get_fare(self,fro,to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(2222,6666)}")

t=Train(1234)
t.book("kathmandu","delhi")
t.get_status()
t.get_fare("kathmandu","delhi")