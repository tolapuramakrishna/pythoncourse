class Employee():
    def __init__(self,name,salary):
        self.name= name
        self.pay = salary
        self.__bonusRate = 12 #private
    
    @property
    def bonusRate(self): #getter
        return self.__bonusRate
    
    @bonusRate.setter
    def bonusRate(self,newRate):
        if newRate >=12 and newRate <=12:
            self.__bonusRate = newRate
        else:
            raise ValueError("value shouldn't be tampered")
            

    def getDetails(self):
        return '{} is having a pay {}'.format(self.name,self.pay)
    
    def getBonus(self):
        return self.pay*(1+self.__bonusRate/100)

e1 = Employee('RK',2000)
print(e1.getDetails())
# print(e1.__bonusRate) #gets error
print(e1.getBonus())
# e1.__bonusRate = 15 #overrides class variable
# print(e1.__bonusRate) #prints 15

print(e1.bonusRate)
e1.bonusRate =10 # throws exception as given in the code