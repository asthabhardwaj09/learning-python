"""Thier are two types of loop
1.for loop
2.while  loop
"""

"""FOR LOOP"""

# For "traversing" a list

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
    for i in x:
        print(i)

# For "String"

a="astha bhardwaj"
for i in a:
    print(i)
    
#Range function 

# output will be 0,1,2,3 beacause of 4-1 
for i in range(4):
    print(i)

 
 #it will start from 2 and end with 14 because 15-1   
for i in range(2,15):
    print(i)

#(start,end,increment)    
for i in range(1,24,5):
    print(i)

"""WHILE LOOP"""

#It execute the statement until the condition is true when condition get false it comes out of the loop

i=int(input("enter the value: "))
while(i<24):
    i=int(input("enter the value: "))
    print(i)
    
print("done with the loop")

'''Else with While Loop
We can even use the else statement with the while loop. 
Essentially what the else statement does is that as soon as the while loop condition becomes False, 
the interpreter comes out of the while loop and the else statement is executed.
'''

count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")


'''break and continue'''

"""break==The break statement enables a program to skip over a part of the code.
A break statement terminates the very loop it lies within."""

for i in range(1,101,1):
    print(i)
    if(i==50):
        break
    pass
print("Thank you")

'''continue 
The continue statement skips the rest of the loop statements and causes the next iteration to occur.
'''
for i in [2,3,4,6,8,0]:
    if (i%2!=0):  #2%2=0!=0  false 1!=0 true
        continue
    print(i)

# do {
  # loop body;
# }while(condition);

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
