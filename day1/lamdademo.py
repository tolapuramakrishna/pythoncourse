'''
add5 = lambda x:x+5
print(add5(4))

square = lambda val: val*val
print(square(5))

sm = lambda name:True if name.startswith('M') else False
print(sm('RK'))


print(type(square))
'''
##=======
#map,sort,filter,reduce
# map(func, *iterable)
names= ['Murthy', 'rk','xyz']
name1 = ('rk','abc')
upper_names = map(lambda val:val.upper(), names) #map object
upper_name1 = map(lambda val:val.upper(), name1) #map object
# print(list(upper_names),name1)

scores = [34,12,23]
# print(list(zip(names,scores))) // can be written in using lambda

results = list(map(lambda x,y:(x,y), names,scores))  #[('Murthy', 34), ('rk', 12), ('xyz', 23)]
# print(results)

result1 = list(map(lambda x,y:(x,y), name1,scores)) # returns [('rk', 34), ('abc', 12)]


##======= filter =====##

scores = [23,24,25,26,9,5,30,55]

evens = list(filter(lambda val:val%2==0,scores))
# print(evens)

def isElgible(score):
    return score>20
isElgible = lambda val:val>20
results = list(filter(isElgible,scores))
# print(results)


## ===== Sort ====##
list1=[('eggs',6),('honey',7),('car',10),('cat',9)]
list1.sort(key=lambda x:x[0],reverse=False)
# print(list1)



##===== reduce =====##

#reduce=reduction theory = from given list,aggregations

from functools import reduce
numbers = [3,4,5,9,33,14]
def sum(first,second):
    return first+second
result = reduce(sum,numbers)
# print(result)


import numpy as np

data = np.array([1,2,3,4,5])
squarer = lambda val:val**2
result = np.array([squarer(xi) for xi in data])

print(result)