# Write a program to estimate runtime of all the function you have used so far.

import time as t
from functionScope import add as fn1
from functionScope import add as fn2


curr = t.time()
print(curr)

def out_func():
    x= 20
    def inn_func():
        x = 30
        print(x)
    
    inn_func()
    print(x)

out_func()
update_time = t.time()
print(update_time)

difference = update_time - curr

res = fn1(6,5)
print(res)
des = fn2(5,1)
print(res)
print(f"\n Time to execute function is {difference/60} min")