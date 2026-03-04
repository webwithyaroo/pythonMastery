"""
    Basic Word Counter
    
    This module provides functionality to count the frequency of user_input based on the input the user gives.
"""
    
# Declare a pure function
def basic_word_counter(user_input: str)-> dict[str, int]:
    
    
    """
    Count the number of occurrence in the given word input
    
    steps:
    - Convert text to lowercase
    - Strip redundant whitespaces
    - Remove punctuations
    - Split user_input
    - Count word frequency(dictionary)
    - Return dictionary
    """
    
    dic = {}
    
    
    #Convert text to lowercase
    normalized_text = user_input.lower().strip()
    
    #Removed Punctuations
    cleaned_text = "".join(char for char in normalized_text if char.isalpha() or char.isspace())
    
    #Split user_input
    splitted_text = cleaned_text.split()
    
    for item in splitted_text:
        if item in dic:
            dic[item]+=1
        else:
            dic[item]=1
            
    print(dic)
    return dic
    

while True:
    user_input = input("how are you doing today: ")
    basic_word_counter(user_input)
    if user_input:
        break
    print("Invalid response, try again")