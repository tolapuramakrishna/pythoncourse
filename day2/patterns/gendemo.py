# Generator and iterator are look a like
# memory can be saved.
# unless we ask it wont process all the loop 

'''
def squarer(nums):
    results =[]
    for i in nums:
        results.append(i*i)
    return results 
# process all item in the list reurns the out
'''
## above code can be replaced with below and runs based on next fn
def squarer(nums):
    for i in nums:
        yield(i*i)

output = squarer([1,2,3,4])
print(type(output))
print(next(output)) #1
print(next(output)) #4
print(output) #<generator object squarer
print(list(output)) #9,16 cuz iterator at 3(2-index)