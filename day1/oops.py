class Employee():
    def __init__(self,name,salary):
        self.name= name
        self.pay = salary
        self.__bonusRate = 12 #private
    
    def getDetails(self):
        return '{} is having a pay {}'.format(self.name,self.pay)
    
    def getBonus(self):
        return self.pay*(1+self.__bonusRate/100)

e1 = Employee('RK',2000)
print(e1.getDetails())
# print(e1.__bonusRate) #gets error
print(e1.getBonus())
e1.__bonusRate = 15 #overrides class variable
print(e1.__bonusRate) #prints 15