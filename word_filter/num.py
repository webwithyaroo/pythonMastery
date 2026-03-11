
# This code demonstrates how to use list comprehension to filter and transform a list of words.


words = ["ai", "machine", "learning", "is", "powerful"]
# result = [word.upper() for word in words if len(word) > 3]
 #print(result)



#numbers = [1,2,3,4]
#item_dict = {num:num*num for num in numbers}
#print(item_dict)



#numbers = [1,2,3,4,5,6]
#result = {num:num**2 for num in numbers if num % 2 == 0}
#print(result)

words = ["ai", "machine", "learning", "is", "powerful"]

filtered = {}

for word in words:
    if len(word) > 3:
        filtered[word] = len(word)
        print(word)



print(filtered)

# output {
#    "machine":7,
#    "learning":8,
#    "powerful":8
# }





numbers = [1,2,3,4,5]
result = {num:"odd" if num % 2 != 0 else "even" for num in numbers }
print(result)



num_type = {}

for num in numbers:
    if num % 2 == 0:
        num_type[num] = "even"
    elif num % 2 != 0:
        num_type[num] = "odd"
        
        
print(num_type)

{
1: "odd",
2: "even",
3: "odd",
4: "even",
5: "odd"
}