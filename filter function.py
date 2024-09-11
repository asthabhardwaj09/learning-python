#filter function

def is_even(a):
    return a%2==0

numbers=[3,4,2,1,5,6,9,8,10]

even=list(filter(is_even,numbers))
print(even)

# with lambda function

evens=list(filter(lambda a:a%2==0,numbers))
print(evens)

evens=filter(lambda a:a%2==0,numbers)
for i in evens:
    print(i)
#map() and filter() function can be iterate only one time
for i in evens:
    print(i)
    
#by list comprehension

new_even=[i for i in numbers if i%2==0]
print(evens)
print(new_even)
    