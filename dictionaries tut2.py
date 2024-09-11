# # add or delete data
# user_info={
#     'name':'astha',
#     'age': 20,
#     'fav_movie':'avengers',
#     'fav_songs':['song1','song2']
# }

# #how to add data
# user_info['fav_tune']=['awakening','fairy tale']
# print(user_info)

# #pop method
# popped_item=user_info.pop('fav_songs')
# print(f"popped item is{popped_item}")
# print(user_info)
# print(type(popped_item)) #type is list because fav songs are in list

# popped_item=user_info.pop('age')
# print(f"popped item is{popped_item}")
# print(user_info)
# print(type(popped_item)) #it will return int because age store integer value

# #popitem method

# popped_item=user_info.popitem()
# # print(user_info)
# print('the popped element is',popped_item)
# print(user_info)
# print(type(popped_item))


# user_info={
#     'name':'astha',
#     'age': 20,
#     'fav_movie':'avengers',
#     'fav_songs':['song1','song2']
# }
# #update dictionary

# more_info={'state':'haryana','hobbies':['coding','reading','guitar']}
# more_info= {'name':'Ravita gautam','state':'haryana','hobbies':['coding','reading','guitar']}

# #when same variable like (name) then it will replace (astha with ravita)

# user_info.update(more_info)
# # user_info.update({})
# print(user_info)

# #fromkeys

# d=dict.fromkeys(('name','age','height'),'unknown')
# d=dict.fromkeys(['name','age','height'],'unknown')
# d=dict.fromkeys ('abc','unknown')
# print(d)

# d=dict.fromkeys(range(1,11),'unknown')
# print(d)

# d=dict.fromkeys(['name','age'],['unknown','unknown'])
# print(type(d))
# print(d)

# #get method(useful)

# d={'name':'astha','age':20}
# print(d['name'])
# # print(d['hobbies'])
# print(d.get('hobbies'))

# # if 'name' in d:
# #     print("present")
# # else:
# #     print("not present")

# if d.get('name'):
#     print("present")
# else:
#     print("not present")    

# # clear method and copy method
# # d.clear()
# # print(d)

# d1=d.copy() #d or d1 alag alag dictionary hai
# # d1=d #same dictionary hai
# # print(d1)
# print(d1.popitem())
# print(d)

# #print(d1 is d)

# #more about get, two same key in dictionaries

# user={'name':'astha','age':20,'fav_hobby':'badmintion'}
# user={'name':'astha','age':20,'fav_hobby':'badmintion','age':34}
# print(user.get('name'))
# print(user.get('age'))
# print(user.get('names','not found'))


'''questions on dictionaries'''

#define a function that take a number(n)
#return a dictionary containing cube of numbers from 1 to n

# a=2**3
# print(a) 

def cube_finder(n):
    for i in range(n):
        cube=(i+1)**3
        print(f"The cube of {i + 1} is: {cube}")
        # print(cube)
cube_finder(5)

def cube_finder(n):
    cubes = {}
    for i in range(1, n + 1): 
        cubes[i] = i ** 3
    return cubes

cubes_dict = (cube_finder(5))
print(cubes_dict)

# word counter in dictionaries 

def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count

print(word_counter('astha bhardwaj'))

'''question 2'''

'''
user={
    'name':'astha'
    'age':20
    'fav_movies':['coco','avengers']
    'fav_songs':['song1',song2]
}

print in the same way by taking the input from the user
'''

user={}

name=input("enter the name: ")
age=input("enter the age: ")
fav_movies=input("enter the fav movie name: ").split(',')
fav_songs=input("enter the fav song: ").split(',')

user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs
# print(user)

for key,value in user.items():
    print(f"{key}:{value}")




