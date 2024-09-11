# def to_power(num,*args):
#     print(args)
#     result=[]
#     for i in args:
#         result.append(i**num)
#     return result
    
# l=[1,2,3]   
# t=to_power(3,*l)   
# print(t) 

def to_power(num, *args):
    if not args:
        return "Hey, you have not passed any args!"
    
    result = []
    for i in args:
        result.append(i**num)
    return result
    
l = [1,2,3]   
t = to_power(3, *l)   
print(t)  




 


     

