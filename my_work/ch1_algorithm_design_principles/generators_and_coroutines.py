# compares the running time of a list compared to a generator

import time


# generator function creates an iterator of odd numbers between n and m
def oddGen(n, m):
    while n < m:
        yield n
        n += 2


# builds a list of odd numbers between n and m
def oddLst(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

# the time it takes to perform sum on an iterator
start1 = time.time()
sum(oddGen(1, 1000000))
print("Time to sum an iterator: %f" %(time.time() - start1))

start2 = time.time()
sum(oddLst(1, 1000000))
print("Time it takes to build and sum a list %f" %(time.time() - start2))

#######################################################################

lst = [1, 2, 3]
gen = (10**i for i in lst)
# generator type
print(type(gen))

# changing it into a list
for i in gen:
    print(i)





