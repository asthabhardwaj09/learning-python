'''    * operator                                         
       * args

'''

def total(a,b):  #normally we use like this
    return a+b
t=total(2,3)
print(t)

def all_total(*args): # if we use * operator than we can take number of argument
    print(args)
all_total(1,2,3,4,5,6,7) #return as tuple

def all_total(*args):
    total=0
    for num in args:
        total+=num
    return total

t=all_total(1,2,3,4,5,6)
print(t)
