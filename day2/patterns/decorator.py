# a function which takes another fn as an parameter is decorator
#intereceptor/broker- higher order function
def broker(func):
    return func('Murthy')

@broker
def say_hello(name):
    return f"hello {name}"

@broker
def appreciate(name):
    return f"Yo {name}, You are excellent"


#without putting @broker decorator below code runs
# print(broker(say_hello)) 
# print(broker(appreciate))

print(say_hello) 
print(appreciate)