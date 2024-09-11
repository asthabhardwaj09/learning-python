#dictionaries intro
# Q:- why we use dictionaries
# A:- because of limitations of lists,lists are not enough to represent
# real data

#example
user=['astha',20,['coco','kimi no na wa'],['awakening','fairy tale']]
print(user)
#this list contains user name,age,fav movie,fav tunes
#you can do this but this is not a good way to do this

#Q:-What are dictionaries
# A:- unordered collections of data in key: value pair

#how to create dictionaries
user= {'name':'astha bhardwaj', 'age':20}
print(user)
print(type(user))

#second method to use dictionaries

user1=dict(name='astha bhardwaj',age=20)
print(user1)
print(type(user))

#how to access data in dictionaries

user= {'name':'astha bhardwaj', 'age':20}
print(user['name'])
print(user['age'])

#which type of data can dictionaries?
# anything
# numbers,strings,list,dictionaries

user_info= {
    'name':'astha bhardwaj',
    'age':20,
    'fav_movie': ['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale'],
}
print(user_info)

# how to add data to empty dictionary

user_info2={}
user_info2['name']='astha'
user_info2['name_2']='simran'
user_info2['age']= 20
user_info2['fav_hobby']='badmintion'
user_info2['fav_singer','fav_actor']='Arjit singh','salman khan'

print(user_info2)
''''''''''''''''''''''''''''''
# in keyword and iteration in dictionary

user_info= {
    'name':'astha bhardwaj',
    'age':20,
    'fav_movie': ['coco','kimi no na wa'],
    'fav_tunes':['awakening','fairy tale'],
}
print(user_info)

if 'names' in user_info:
    print('present')
else:
    print('not present')

#check if value exits in dictionary
if ['coco','kimi no na wa'] in user_info.values():
    print('present')
else:
    print('not present')

if 'astha bhardwaj' in user_info.values():
    print('present')
else:
    print('not present')

# loop in dictionary

for i in user_info: #return key
    print(i)

for i in user_info.values(): #return value
    print(i)
    
#values method
user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

s=user_info.values()
print(s)

#key method
user_info_keys=user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

s=user_info.keys()
print(s)
print(type(s))

#loop in dictionaries
for i in user_info:   #it will gives values
    print(user_info[i])

#item method
user_items=user_info.items()
print(user_items)
print(type(user_info))

for i,j in user_info.items():
# for i in user_info.items():
    print(f"key is {i} and value is {j}")
    # print(i)










