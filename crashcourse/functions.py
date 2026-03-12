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