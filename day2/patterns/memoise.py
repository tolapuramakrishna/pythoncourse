def memoize(func):
    memo={}
    def wrapper(x):
        if x not in memo:
            memo[x]=func(x)
        return memo[x]
    return wrapper

@memoize
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print("Please wait")
print(fib(40))