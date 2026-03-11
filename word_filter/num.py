
# This code demonstrates how to use list comprehension to filter and transform a list of words.


words = ["ai", "machine", "learning", "is", "powerful"]
# result = [word.upper() for word in words if len(word) > 3]
 #print(result)



#numbers = [1,2,3,4]
#item_dict = {num:num*num for num in numbers}
#print(item_dict)



numbers = [1,2,3,4,5,6]
result = {num:num**2 for num in numbers if num % 2 == 0}
print(result)

