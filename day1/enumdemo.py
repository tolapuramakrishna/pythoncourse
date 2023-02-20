# enumrations are string constants
#Enum
from enum import Enum

class Status(Enum): #inherting Enum into Status (inheritence)
    WORKING =1
    SUSPENDED = 2
    ON_BENCH = 3
## ZOMATO - PREPARING, ORDERING, ON_THE_WAY, DELIVERED

state = Status.WORKING
print(state.name)
print(state.value)
newstate = state.value+1
if(newstate ==2):
    print("Employee is suspended!")