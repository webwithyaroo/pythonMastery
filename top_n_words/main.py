"""
    This module uses a function to evaluate the top 3 most frequent words as a list of turples
"""

def counter(user_input: str)-> list[tuple, int]:
    """ A program that takes user_input as argument and return the top most frequent words as a list[] of turples(words, count) 

    Args:
        user_input (str): The user input to be processed and analyzed

    Returns:
        list[tuple,int]: The final expected result after analyses is completed
    """
    
    frequency = {}
    
    
    normalized_text = user_input.lower().strip()
    cleaned_text = "".join(char for char in normalized_text if char.isalpha() or char.isspace())
    splitted_text = cleaned_text.split()
    
    for word in splitted_text:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
            
    item_list = frequency.items()
    print(item_list)
    return frequency

if __name__ == "__main__":
    
    while True:
        user_input = input("Provide input as text: ")
        if user_input:
            result = counter(user_input)
            break
        print("Invalid response")