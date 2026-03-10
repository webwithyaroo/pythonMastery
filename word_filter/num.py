
# This code demonstrates how to use list comprehension to filter and transform a list of words.


words = ["ai", "machine", "learning", "is", "powerful"]
result = [word.upper() for word in words if len(word) > 3]
print(result)



numbers = [1,2,3,4]
items_dict = {num:num*num for num in numbers}

print(items_dict)
