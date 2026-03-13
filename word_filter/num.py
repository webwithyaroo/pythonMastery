
# This code demonstrates how to use list comprehension to filter and transform a list of words.



"""
    This module explains how a functions should handle multiple arguments
"""

def counter(text: str, min_word = 3)-> dict[str, int]:
   
    """ This is a function that takes 2 arguments, analyzes the text and return a dictionary showing the frequency of the words

    Arg:
        (text: str, min_word = 3):Takes in 2 arguments 
    
    Returns:
        dict[str, int]:The expected result after analyses
    """
    normalized_text = text.lower()
    cleaned_text = "".join(text for text in normalized_text if text.isspace() or text.isalpha())
    split_text = cleaned_text.split()
    
    word_check = [word for word in split_text if len(word) > min_word ]
    
    frequency = {}
    
    for word in word_check:
        if word in frequency:
            frequency[word]+=1
            
        else:
            frequency[word]=1
    
    
    return frequency
    
    
if __name__ == "__main__":
    while True:
        user_input = input("Input: ")
        if user_input:
            result = counter(user_input, 5)
            print(result)
            break
        print("Invalid input")







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





