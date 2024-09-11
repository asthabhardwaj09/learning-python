# Question

#define a function take any number of  lists containing number
# [1,2,3] , [4,5,6] , [7,8,9]
# return average
# (1+4+7)/3  (2+5+8)/3  (3+6+9)/3
# try make this anonymous function in one line using lambda


def average_finder(*args):
    result=[]
    print(args)
    for nums in zip(*args):
        avg = sum(nums) / len(nums)
        result.append(avg)
        
    return result
        
#(1+4+7)/3     (2+5+8)/3      (7+8+9)/3 
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]

total_average=average_finder(l1,l2,l3)
print(total_average)


#for example
num=[1,2,3]
print(num) #pack
print(*num) #unpack

''''''''''''''''''''''''''''''''''''

average_finder=lambda *args:[sum(nums)/len(nums) for nums in zip(*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9]))








