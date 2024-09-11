#we use enumerate function with for loop to track position of our iteam in iterable 

#how can we do this without enumerate function
name=['abc','abcdf','xyz']
pos=0
for names in name:
    print(f"{pos} -------> {names}")
    pos+=1
    
#with enumarate function
for pos,names in enumerate(name):
    print(f"{pos} ----> {names}")
    
#Question

'''
define a function that take two arguments
1. list containing string
2. string that want to find in your list
and this function will return the index of string in your list 
and if string is not present then return -1
'''  

def find_pos(l,target):
    for pos,name in enumerate(l):
#enumerate(l) generates pairs of (pos, name) ,,  enumerate(name) we can write like this also
        if name==target:
            return pos   
    return -1
names=['astha','ravita','harshit']
print(find_pos(names,'ravita'))

# a=['astha','abc','scg']
# print(a[0])

