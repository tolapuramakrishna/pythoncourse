#order.py
class Ordering:
    def orderFood(self):
        print("order food")
    
    def cancelOrder(self):
        print("yoour order canceled")

##------##
# prepare.py
class Preaparing:
    def preapredFood(self):
        print("food is getting prepared.. ")

##---##
# deliver.py
class Delivering:
    def deliverFood(self):
        print("food is on the way, track it...")


####----##
#wrapper= facade-frontend controller

class Operator():
    def __init__(self):
        self.ordering=Ordering()
        self.preparing = Preaparing()
        self.delivering = Delivering()
        print("food delivery - open")
    
    def placeOrder(self):
        import time
        time.sleep(2)
        self.ordering.orderFood()
        time.sleep(4)
        self.preparing.preapredFood()
        time.sleep(6)
        self.delivering.deliverFood()

##------##
if __name__=='__main__':
    op = Operator()
    op.placeOrder()
    print("enjoy the food")

# we should have everything in singleton objects
