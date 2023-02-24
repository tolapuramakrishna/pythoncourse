import time
#custom logger decorator
def profiler(fp):
    def wrapper_timer(*args,**kwargs):
        start = time.perf_counter()
        value = fp(*args,**kwargs)
        end = time.perf_counter()
        runtime = end- start
        print(f"Finsihed {fp.__name__} in {runtime:.4f} secs")
        return value
    return wrapper_timer
###---##

@profiler
def complex_task(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000) ])

complex_task(1)
complex_task(999)