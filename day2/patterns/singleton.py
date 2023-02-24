# singleton - how to create single global access point (instance)
# like Db connection, logger, Authentications, API gateway, http context, cache management, config file manager

class BankSingleton:
    __instance__ = None

    def __init__(self):
        if BankSingleton.__instance__ is None:
            BankSingleton.__instance__ = self
        else:
            raise Exception("Instance is already created..")
    
    @staticmethod
    def getInstance():
        if not BankSingleton.__instance__:
            BankSingleton()
    
        return BankSingleton.__instance__

    def getBalance(self,acno):
        return f"Account no {acno} balance: 60000"

if __name__ == '__main__':
    '''
    bank1 = BankSingleton()
    print(bank1.getBalance(101))
    # bank2= BankSingleton() #exception will triggred
    # print
    '''
    b1 = BankSingleton.getInstance()
    print(b1)
    print(b1.getBalance(101))
    b2 = BankSingleton.getInstance()
    print(b2)

    b3 = BankSingleton() #throws error
'''
if __name__ == '__main__':
    b3 = BankSingleton() # craetes instance
    b1 = BankSingleton.getInstance()
    print(b1)
    print(b1.getBalance(101))
    b2 = BankSingleton.getInstance()
    print(b2)
'''

    