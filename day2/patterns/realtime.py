import random,time

customers=['Raj','kumar','virat','jadeja']

ac_types= ['Savings','Current','FD','Homeloan']

def custmoer_list(people):
    result =[]
    for i in range(people):
        customer = {
            'id':i,
            'name':random.choice(customers),
            'acType':random.choice(ac_types)
        }
        result.append(customer)
    return result
#=======
def customer_generator(people):
    for i in range(people):
        customer = {
            'id':i,
            'name':random.choice(customers),
            'acType':random.choice(ac_types)
        }
        yield customer    
#======
if __name__ == '__main__':
    start = time.process_time()
    people = custmoer_list(100000)
    end = time.process_time()

    print(f"Time taken with list: {end-start} secs") #0.5

#clearing memory - garbage 
    import gc
    del people
    gc.collect

    start = time.process_time()
    people = customer_generator(100000) # 0.0 secs cuz only reocrd
    end = time.process_time()

    print(f"Time taken with generator: {end-start} secs")  #0.0 secs cuz only reocrd
    #people = list(customer_generator(100000)) # this will again take 0.5 secs