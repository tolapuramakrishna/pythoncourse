#for internally used for iterator

'''
nums = [3,2,5,6,8] #iterable object
for i in nums: #iterator
    print(i)

print(type(nums)) #class list
it=iter(nums)
print(type(it)) # class list_iterator
print(it.__next__()) #3
print(it.__next__()) #2
print(next(it)) #5
'''
#custom iterator
'''
pandas 
pd.head() - gives first 5 items
pd.tail() - gives last 5 items
pd.head(10) - gives first 10 items
'''
#custom iterator
class Head(object):
    def __init__(self):
        self.num = 1

    def __iter__(self):  #overriding iter fn
        return self
    
    def __next__(self):
        #api cal to rest api or get data from db 
        if self.num<=5:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration

if __name__ == '__main__':
    values = Head()
    print(values.__next__())#prints 1
    print(values.__next__())#2
    for i in values: # prints 3,4,5,
        print(i)