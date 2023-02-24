def logger(func):
    def wrapper(): #inner function
        print(f"Log: someone called {func.__name__} function")
        func()
        print(f"Log: {func.__name__} function is excuted")
    return wrapper
##==========
@logger
def task():
    print("Murty")

task()