#dictionary comprehension 
#square={1:1 2:4 3:9}

# square={num:num**2 for num in range(1,11)}
# print(square)

square={f"square of {num} is":num**2 for num in range(1,11)}
print(square)
for k,v in square.items():
    print(f"{k} : {v}")
    
#"astha"

str='astha'
word_count={char:str.count(char) for char in str}
print(word_count)

#dictionary comprehension with if else
#d={1:'odd' , 2:'even'}

odd_even= {i:('even' if i%2==0 else 'odd')for i in range(1,11)}
print(odd_even)